---
layout: post
title:  "Kuya: 1"
excerpt: boot2root by @syedashhad
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
3 flags / root

## Download #
[https://www.vulnhub.com/entry/kuya-1,283/](https://www.vulnhub.com/entry/kuya-1,283/)

## Walkthrough #
**nmap**
<br>![alt text](../vulnhub/Kuya_1/nmap.png)
<br><br>
**default 80**
<br>![alt text](../vulnhub/Kuya_1/default80.png)
<br><br>
**default 80 sources...trolls**
<br>![alt text](../vulnhub/Kuya_1/default80source.png)
<br><br>
**gobuster reveals some directories**
<br>![alt text](../vulnhub/Kuya_1/gobuster.png)
<br><br>
**wordpress is a wash**
<br>![alt text](../vulnhub/Kuya_1/wordpress.png)
<br><br>
**loot gives some images to investigate**
<br>![alt text](../vulnhub/Kuya_1/loot80.png)
<br><br>
**steghide extract on the images gives some files, no password needed**
<br>![alt text](../vulnhub/Kuya_1/steghide.png)
<br><br>
**secret.txt...troll**
<br>![alt text](../vulnhub/Kuya_1/secrettxt.png)
<br><br>
**emb.txt...brainfuck**
<br>![alt text](../vulnhub/Kuya_1/embtxt.png)
<br><br>
**flag 1 is revealed**
<br>![alt text](../vulnhub/Kuya_1/flag1.png)
<br><br>
**flag 1 base64 decoded**
<br>![alt text](../vulnhub/Kuya_1/bfbalut.png)
<br><br>
**loot.pcapng reveals 7z file**
<br>![alt text](../vulnhub/Kuya_1/lootpcap.png)
<br><br>
**export from pcap**
<br>![alt text](../vulnhub/Kuya_1/exportpcap.png)
<br><br>
**7z file is password protected**
<br>![alt text](../vulnhub/Kuya_1/7zpassprotect.png)
<br><br>
**let's look at the contents, private key. nice**
<br>![alt text](../vulnhub/Kuya_1/7zcontents.png)
<br><br>
**let's brute force**
<br>![alt text](../vulnhub/Kuya_1/lootbrutejohn.png)
<br><br>
**using found password, it works**
<br>![alt text](../vulnhub/Kuya_1/7zloot.png)
<br><br>
**using the priv key, it seems it's password protected**
<br>![alt text](../vulnhub/Kuya_1/idrsapassprotect.png)
<br><br>
**we brute force and find the password**
<br>![alt text](../vulnhub/Kuya_1/idrsabrutejohn.png)
<br><br>
**with that we get a shell**
<br>![alt text](../vulnhub/Kuya_1/shell.png)
<br><br>
**flag 2 found**
<br>![alt text](../vulnhub/Kuya_1/flag2.png)
<br><br>
**searching around, file date stands out in wordpress directory**
<br>![alt text](../vulnhub/Kuya_1/wpdate.png)
<br><br>
**wordpress config reveals db password**
<br>![alt text](../vulnhub/Kuya_1/wpconfig.png)
<br><br>
**trying same password for kuya works**
<br>![alt text](../vulnhub/Kuya_1/kuya.png)
<br><br>
**flag 3 revealed**
<br>![alt text](../vulnhub/Kuya_1/flag3.png)
<br><br>
**checking .bash_history we find some special commands**
<br>![alt text](../vulnhub/Kuya_1/bashhist.png)
<br><br>
**after some googling, we verify what is found in .bash_history will work to read /etc/shadow**<br>
[https://nxnjz.net/08/an-interesting-privilege-escalation-vector-getcap/](https://nxnjz.net/08/an-interesting-privilege-escalation-vector-getcap/)
<br>![alt text](../vulnhub/Kuya_1/shadow.png)
<br><br>
**so many different tries for root after recovering files**
<br>![alt text](../vulnhub/Kuya_1/trying.png)
<br><br>
**turns out you just do the entire folder...root flag**
<br>![alt text](../vulnhub/Kuya_1/root.png)
<br><br>













