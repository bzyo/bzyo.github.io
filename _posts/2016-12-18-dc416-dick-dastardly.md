---
layout: post
title:  "DC416: 2016 - Dick Dastardly"
excerpt: CTF by @_RastaMouse
tags: [vulnhub, ctf, walkthrough]
---

# DC416: 2016 - Dick Dastardly

## Goal 
Capture all 4 flags in flag{} format

## Download 
[https://www.vulnhub.com/entry/dc416-2016,168/](https://www.vulnhub.com/entry/dc416-2016,168/)

## Walkthrough 
Initial nmap reveals ssh on 22, web server running on 80 and irc on 6667
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-nmap.png)
<br><br>

Running dirb against site shows two separate index pages, index.html and index.php
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-dirb.png)
<br><br>

index.html is the default DC416 rules
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-indexhtml.png)
<br><br>

index.php shows a guestbook and login area
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-indexphp.png)
<br><br>

Preparing the site to run through burp suite to attempt a SQLi attack, flag 1 is revealed
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-flag1.png)
<br><br>
flag1{l0l_h0w_345y_15_7h15_c7f}

With no known credentials, I setup burp to run a SQLi attack
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-sqli002.png)
<br><br>

After a short while, a payload of  ' or 0=0 # is revealed and shows admin is logged into the site
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-sqli004.png)
<br><br>

Using the SQLi payload on index.php, admin.php page is revealed
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-adminarea.png)
<br><br>

With three options, I decide to act on all of them
Adding IP to IRC whitelist simply refreshes the page, but burp shows a post to activate
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-supybotactivate.png)
<br><br>

I add a simple supybot owner with username yoyo and password 1234
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-addsupybot.png)
<br><br>

After adding a user, I activate supybot
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-activate.png)
<br><br>

Knowing IRC port is open, I attempt connecting using irssi with command /connect 192.168.0.133 and it's successful
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-irssi001.png)
<br><br>

No channels or users are known, so I send a /list command which reveals the channel #vulnhub
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-irssi002.png)
<br><br>

Joining the channel reveals the user vulnhub-bot
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-irssi003.png)
<br><br>

Using the added username yoyo, I message the user with /msg vulnhub-bot user identify yoyo 1234 and it's successful
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-irssi004.png)
<br><br>

Running list reveals various commands that can be run including unix shell which allows system access, directory listing and reveals flag 2
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-irssi005.png)
<br><br>
flag2{y0u'r3_4_5upyb07_n00b_m8}

Being able to run system commands I attempt a reverse shell...
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-reverseshell001.png)
<br><br>

...and it's successful
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-reverseshell002.png)
<br><br>

Some initial file enumeration shows a file xss.js stores the credentials for the admin.php page
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-xss.png)
<br><br>
rasta:1b37y0uc4n76u3557h15p455w0rd,5uck3rz

Some additional enumeration shows mysql root credentials by running crontab -l
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-crontab.png)
<br><br>
root:vulnhub

Using the mysql credentials reveals nothing special
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-mysql.png)
<br><br>

Additional enumeration by running ps -aux reveals an interesting ping command being run as root with a pattern (-p) option
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-psaux001.png)
<br><br>

After running ps -aux several other times it seems that the pattern changes every so often
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-ping001.png)
<br><br>

I start wireshark and notice icmp traffic from the system. Filtering traffic to icmp only reveals the ping pattern seen from ps -aux. Each packet has text data which when put together reveals flag 0

flag0{the_quiete
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-ws001.png)
<br><br>

r_you_become_the
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-ws002.png)
<br><br>

_more_you_are_ab
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-ws003.png)
<br><br>

le_to_hear}
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-ws004.png)
<br><br>

flag0{the_quieter_you_become_the_more_you_are_able_to_hear}
So now I only have one additional flag as they apparently started at zero :)

Additional enumeration shows that current user rasta can sudo as vulnhub with no password for a specific command
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-sudo001.png)
<br><br>

Running the command reveals nothing as it's a limited shell. After many various attempts, the letter q actually quits the program and reveals the menu
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-pyutil001.png)
<br><br>

Option 1 reveals the user, which is vulnhub, Option 2 didn't do anything at first, but after several attempts it seems you have to specify the directory you would like listed. This reveals that /home/vulnhub holds the last flag
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-pyutil002.png)
<br><br>

Option 3 actually holds coffee :)
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-pyutil003.png)
<br><br>

After several failed attempts, I found the correct way to reveal flag 3
<br>![alt text](../vulnhub/DC416_2016-DickDastardly/v4dick-flag3.png)
<br><br>

flag3{n3x7_71m3_54n17153_y0ur_1npu7}
