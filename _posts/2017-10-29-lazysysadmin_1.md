---
layout: post
title:  "LazySysAdmin: 1"
excerpt: CTF by @TogieMcdogie
tags: [vulnhub, ctf, walkthrough]
---

# LazySysAdmin: 1

## Goal
uid=0(root) gid=0(root) groups=0(root)

## Download 
[https://www.vulnhub.com/entry/lazysysadmin-1,205/](https://www.vulnhub.com/entry/lazysysadmin-1,205/0)

## Walkthrough 
Initial nmap shows ports open on 22, 80, 139, 445 and 3306
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-nmap-000.png)
<br><br>

Nothing special with web page as the links don't work and nothing in source
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-web-001.png)
<br><br>

nikto reveals a wordpress instance and after some enumeration the most we got was a username 'togie'
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-nikto-002.png)
<br><br>

wpscan reveals latest version of wordpress nothing more after further enumeration
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-wpscan-005.png)
<br><br>

Went back to open smb ports and enumerated open shares using nmap script
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-smbenum-006.png)
<br><br>

Using smbclient we're able to get full read-only access to www folder and it shows a file deets.txt
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-smbclient-008.png)
<br><br>

Opening deets.txt up in a browser reveals a password
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-deets-009.png)
<br><br>

Using that password with found username togie, we have a shell
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-togie-010.png)
<br><br>

Simple sudo -i elevates us to root
<br>![alt text](../vulnhub/2017/LazySysAdmin_1/imgs/lazy-root-011.png)
<br><br>