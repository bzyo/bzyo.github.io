---
layout: post
title:  "vulnhub walkthrough: kuya: 1"
excerpt: boot2root by @syedashhad
---

# Kuya: 1

## Goal #
3 flags / root

## Download #
[https://www.vulnhub.com/entry/kuya-1,283/](https://www.vulnhub.com/entry/kuya-1,283/)

## Walkthrough #
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>
**default 80**
<br>![alt text](imgs/default80.png)
<br><br>
**default 80 sources...trolls**
<br>![alt text](imgs/default80source.png)
<br><br>
**gobuster reveals some directories**
<br>![alt text](imgs/gobuster.png)
<br><br>
**wordpress is a wash**
<br>![alt text](imgs/wordpress.png)
<br><br>
**loot gives some images to investigate**
<br>![alt text](imgs/loot80.png)
<br><br>
**steghide extract on the images gives some files, no password needed**
<br>![alt text](imgs/steghide.png)
<br><br>
**secret.txt...troll**
<br>![alt text](imgs/secrettxt.png)
<br><br>
**emb.txt...brainfuck**
<br>![alt text](imgs/embtxt.png)
<br><br>
**flag 1 is revealed**
<br>![alt text](imgs/flag1.png)
<br><br>
**flag 1 base64 decoded**
<br>![alt text](imgs/bfbalut.png)
<br><br>
**loot.pcapng reveals 7z file**
<br>![alt text](imgs/lootpcap.png)
<br><br>
**export from pcap**
<br>![alt text](imgs/exportpcap.png)
<br><br>
**7z file is password protected**
<br>![alt text](imgs/7zpassprotect.png)
<br><br>
**let's look at the contents, private key. nice**
<br>![alt text](imgs/7zcontents.png)
<br><br>
**let's brute force**
<br>![alt text](imgs/lootbrutejohn.png)
<br><br>
**using found password, it works**
<br>![alt text](imgs/7zloot.png)
<br><br>
**using the priv key, it seems it's password protected**
<br>![alt text](imgs/idrsapassprotect.png)
<br><br>
**we brute force and find the password**
<br>![alt text](imgs/idrsabrutejohn.png)
<br><br>
**with that we get a shell**
<br>![alt text](imgs/shell.png)
<br><br>
**flag 2 found**
<br>![alt text](imgs/flag2.png)
<br><br>
**searching around, file date stands out in wordpress directory**
<br>![alt text](imgs/wpdate.png)
<br><br>
**wordpress config reveals db password**
<br>![alt text](imgs/wpconfig.png)
<br><br>
**trying same password for kuya works**
<br>![alt text](imgs/kuya.png)
<br><br>
**flag 3 revealed**
<br>![alt text](imgs/flag3.png)
<br><br>
**checking .bash_history we find some special commands**
<br>![alt text](imgs/bashhist.png)
<br><br>
**after some googling, an interesting find seems to work to read /etc/shadow**<br>
[https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/](https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/)
<br>![alt text](imgs/shadow.png)
<br><br>















