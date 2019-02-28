---
layout: post
title:  "Hackday Albania"
excerpt: CTF by @r_73en
tags: [vulnhub, ctf, walkthrough]
---

## Goal 
root access + flag.txt

## Download 
[https://www.vulnhub.com/entry/hackday-albania,167/](https://www.vulnhub.com/entry/hackday-albania,167/)

## Walkthrough 
Initial nmap reveals a web server running on 8008 and ssh on port 22
<br>![alt text](../vulnhub/Hackday_Albania/hackday-nmap.png)
<br><br>

Website reveals Mr. Robot and a message that translates to "If I am, I know where to go ;)"
<br>![alt text](../vulnhub/Hackday_Albania/hackday-initial001.png)
<br><br>

Checking the source code there's a message that translates to "but not here"
<br>![alt text](../vulnhub/Hackday_Albania/hackday-initial002.png)
<br><br>

Running nikto shows various directories found from robots.txt file
<br>![alt text](../vulnhub/Hackday_Albania/hackday-nikto.png)
<br><br>

Browsing to the first directory listed, it prompts with the translated message "Is this a proper directory or a jerk" < LOL I hope that Google translation is accurate
<br>![alt text](../vulnhub/Hackday_Albania/hackday-hmmm.png)
<br><br>

With a lot of directories to go through, I decided to save the directories listed in robots.txt to a file and run through dirb
<br>![alt text](../vulnhub/Hackday_Albania/hackday-robots.png)
<br><br>

Running the directories through dirb reveals that /unisxcudkqjydw is a different size. So let's try that...
<br>![alt text](../vulnhub/Hackday_Albania/hackday-dirb.png)
<br><br>

Browsing this directory reveals another hint
<br>![alt text](../vulnhub/Hackday_Albania/hackday-vulnbank.png)
<br><br>

Adding /vulnbank to the original URL reveals a directory listing
<br>![alt text](../vulnhub/Hackday_Albania/hackday-client.png)
<br><br>

Clicking the client folder reveals a Very Secure Bank login page
<br>![alt text](../vulnhub/Hackday_Albania/hackday-verysecure.png)
<br><br>

With no known credentials, I setup burp suite to run a SQLi attack against
<br>![alt text](../vulnhub/Hackday_Albania/hackday-burp001.png)
<br><br>

Quick turnaround and two possible payloads
<br>![alt text](../vulnhub/Hackday_Albania/hackday-burp002.png)
<br><br>

Tested both on the username, and they both login as Charles D. Hobson
<br>![alt text](../vulnhub/Hackday_Albania/hackday-loggedin001.png)
<br><br>

Scrolling over on the page reveals a place to upload files...
<br>![alt text](../vulnhub/Hackday_Albania/hackday-loggedin002.png)
<br><br>

First thought was to upload a php reverse shell, but states that only specific image files are allowed
<br>![alt text](../vulnhub/Hackday_Albania/hackday-upload001.png)
<br>![alt text](../vulnhub/Hackday_Albania/hackday-upload001a.png)
<br><br>

Simply adding .jpg to the end of the shell file and trying again results in...upload success!
<br>![alt text](../vulnhub/Hackday_Albania/hackday-upload002.png)
<br>![alt text](../vulnhub/Hackday_Albania/hackday-upload002a.png)
<br><br>

Next I setup meterpreter, browse to the newly uploaded file and...BOOM limited shell!
<br>![alt text](../vulnhub/Hackday_Albania/hackday-shell.png)
<br><br>

Connected as www-data gives limited access so let the enumeration begin. First I see what is available in the /home directory...nothing. However it gives us a username taviso < i get it
<br>![alt text](../vulnhub/Hackday_Albania/hackday-taviso.png)
<br><br>

Next checking /var/www/html it becomes obvious that all files are readable and belong to the user taviso. Browsing to the directory that provided access shows a config.php file
<br>![alt text](../vulnhub/Hackday_Albania/hackday-www.png)
<br><br>

Viewing the config.php file gives us the mysql root password
<br>![alt text](../vulnhub/Hackday_Albania/hackday-config.png)
<br><br>

Looking at mysql doesn't provide much more information other than two logins to the site. Moving on...
<br>![alt text](../vulnhub/Hackday_Albania/hackday-mysql.png)
<br><br>

Checking permissions on /tmp shows the obvious of full access and I upload both the python and bash linux privilege checker scripts. Seems python isn't available, only python 3 and 3.5 which do not work with the python script.  However the bash script works and pays off as it reveals /etc/passwd is writable!
<br>![alt text](../vulnhub/Hackday_Albania/hackday-passwd.png)
<br><br>

Since I'm able to update any user, including root, I quickly check /etc/sshd_config file and it states that remote access isn't available with password. Oh well...
<br>![alt text](../vulnhub/Hackday_Albania/hackday-sshd_config.png)
<br><br>

So first I create a password hash using openssl
<br>![alt text](../vulnhub/Hackday_Albania/hackday-openssl.png)
<br><br>

Using the meterpreter session, I download the /etc/passwd file and update root and taviso passwords
<br>![alt text](../vulnhub/Hackday_Albania/hackday-passwdupdate.png)
<br><br>

Back to meterpreter, I upload the updated file replacing the original and check to see it's the newer version
<br>![alt text](../vulnhub/Hackday_Albania/hackday-passwdupdate2.png)
<br><br>

Now with my own password set on taviso, ssh access to the system works. From there issuing su with the new password gives root access.  In the root folder is a message that translates to "Congratulations, now launches report".  Also available is the file flag.txt with an MD5 hash of d5ed38fdbf28bc4e58be142cf5a17cf5 that decodes to rio
<br>![alt text](../vulnhub/Hackday_Albania/hackday-root.png)