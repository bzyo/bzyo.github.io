---
layout: post
title:  "RickdiculouslyEasy: 1"
excerpt: CTF by @LhHillz
tags: [vulnhub, ctf, walkthrough]
---

## Goal 
130 Points<br>
uid=0(root) gid=0(root) groups=0(root)

## Download 
[https://www.vulnhub.com/entry/rickdiculouslyeasy-1,207/](https://www.vulnhub.com/entry/rickdiculouslyeasy-1,207/)

## Walkthrough 
**Initial nmap on all ports reveals the following open ports: 21, 22, 80, 9090, 13337, 22222, 60000.  The scan finds two flags immediately, but let's verify to make sure we're not missing anything.**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_nmap1-000.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_nmap2-000.png)
<br><br>
**Connecting to FTP using anonymous we're able to download FLAG.txt, but unable to upload any files**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_ftp-001.png)
<br><br>
**First flag revealed**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag1-002.png)
<br><br>
**FLAG{Whoa this is unexpected}**<br>
**Points = 10**<br>
**Overall points = 10**<br><br>
**SSH seems fake as it is unable to connect, moving on**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_ssh-003.png)
<br><br>
**Checking out Morty's Cool Website, nothing interesting and nothing in source**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-004.png)
<br><br>
**Running dirb against finds some interesting paths**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_dirb-005.png)
<br><br>
**The passwords directory reveals new flag and another page**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-006.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag2-007.png)
**FLAG{Yeah d- just don't do it.}**<br>
**Points = 10**<br>
**Overall points = 20**<br><br>
**The passwords.html page is nothing special**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-008.png)
<br><br>
**But the source reveals a password winter**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-009.png)
<br><br>
**Looking at robots.txt, it shows some interesting files are located in cgi-bin**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-010.png)
<br><br>
**File root_shell.cgi is too good to be true**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-011.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-012.png)
<br><br>
**File tracertool.cgi however looks promising** 
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_tracer-013.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_tracer2-014.png)
<br><br>
**Seems that command injection is possible and we get /etc/passwd**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_cmdinj-015.png)
<br><br>
**After messing around with this for way too long, I found that it wasn't a way in. However I did find that that cat command just printed a cat and less needed to be used :)**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_web-016.png)
<br><br>
**Also found that the /etc/passwd file was false, as looking at /etc/group reveals the usernames we need; RickSanchez, Morty, Summer**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_webgroup-017.png)
<br><br>
**We'll come back to user credentials after covering all these other open ports.**
<br><br>
**Let's start with port 9090 in a web browser, which gives us another flag.  Nothing else to do as password field and submit button are missing**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag3-018.png)
<br><br>
**FLAG {There is no Zeus, in your face!}**<br>
**Points = 10**<br>
**Overall points = 30**<br><br>
**Next port is 13337, which we netcat to revealing another flag and nothing else**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag4-019.png)
<br><br>
**FLAG:{TheyFoundMyBackDoorMorty}**<br>
**Points = 10**<br>
**Overall points = 40**<br><br>
**Next port is 60000, that holds a flag and no other commands work**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag5-020.png)
<br><br>
**FLAG{Flip the pickle Morty!}**<br>
**Points = 10**<br>
**Overall points = 50**<br><br>
**Now onto port 22222, the real SSH port.  So we found a password 'winter' and we have a username 'Summer'....uh let's try that. BOOM, we have access and another flag**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_ssh-021.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag6-022.png)
<br><br>
**FLAG{Get off the high road Summer!}**<br>
**Points = 10**<br>
**Overall points = 60**<br><br>
**Looking around we have two more home directories; Morty and RickSanchez. Since we know RickSanchez is part of the wheel group, let's start with Morty.**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_home-023.png)
<br><br>
**We reveal two files so we sftp them off to kali**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_sftp-024.png)
<br><br>
**Looking at the file Safe_Password.jpg, looking good Rick :)**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_pic-025.png)
<br><br>
**Nothing special so we throw it at strings, which reveals the password for the zip**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_safepass-026.png)
<br><br>
**Using the found password we're able to unzip the file and reveal another flag and an interesting message**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag7-027.png)
<br><br>
**FLAG: {131333}**<br>
**Points = 20**<br>
**Overall points = 80**<br><br>
**Looking at RickSanchez home folder we find two folders.  Trying RICKS_SAFE we find an executable named safe, but it's unable to run so we sftp to kali**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_safe1-029.png)
<br><br>
**The other folder, obviously fake, but I had to look...**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_notflag1-028.png)
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_notflag-028.png)
<br><br>
**Back to the safe executable file, seems that it needs an argument to run.  Putting it to strings it seems that it's going to need that argument to decrypt the message**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_safearg-030.png)
<br><br>

**Sending all A's reveals the encrypted message**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_decrypt-031.png)
<br><br>
**Looking back at the last flag and message, I try the number as the arguments or key.  With that the message is decrypted revealing another hint and flag**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag7-032.png)
<br><br>
**FLAG{And Awwwaaaaayyyy we Go!}**<br>
**Points = 20**<br>
**Overall points = 100**<br><br> 

**So we know the parameters needed for user RickSanchez.  First we Google what band Rick was in, seems to be 'The Flesh Curtains'.  Next we use crunch to generate the 1 Uppercase character and 1 Digit, outputting to a file.  Last we append the word Flesh and Curtains to that created listed by using sed and outputting to two new files**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_crunchsed-032.png)
<br><br>
**Last we throw those files at hydra and we get the password on the second list**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_hydra-034.png)
<br><br>
**With that we're able to SSH as RickSanchez and with a simple 'sudo -i' we're root :)**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_root-035.png)
<br><br>
**Last flag is revealed giving us 130 points**
<br>![alt text](../vulnhub/RickdiculouslyEasy_1/rick_flag8-036.png)
<br><br>
**FLAG: {Ionic Defibrillator}**<br>
**Points = 30**<br>
**Overall points = 130**
