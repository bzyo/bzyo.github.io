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
<br>![alt text](../vulnhub/2018/kuya_1/imgs/nmap.png)
<br><br>
**default 80**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/default80.png)
<br><br>
**default 80 sources...trolls**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/default80source.png)
<br><br>
**gobuster reveals some directories**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/gobuster.png)
<br><br>
**wordpress is a wash**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/wordpress.png)
<br><br>
**loot gives some images to investigate**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/loot80.png)
<br><br>
**steghide extract on the images gives some files, no password needed**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/steghide.png)
<br><br>
**secret.txt...troll**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/secrettxt.png)
<br><br>
**emb.txt...brainfuck**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/embtxt.png)
<br><br>
**flag 1 is revealed**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/flag1.png)
<br><br>
**flag 1 base64 decoded**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/bfbalut.png)
<br><br>
**loot.pcapng reveals 7z file**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/lootpcap.png)
<br><br>
**export from pcap**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/exportpcap.png)
<br><br>
**7z file is password protected**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/7zpassprotect.png)
<br><br>
**let's look at the contents, private key. nice**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/7zcontents.png)
<br><br>
**let's brute force**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/lootbrutejohn.png)
<br><br>
**using found password, it works**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/7zloot.png)
<br><br>
**using the priv key, it seems it's password protected**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/idrsapassprotect.png)
<br><br>
**we brute force and find the password**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/idrsabrutejohn.png)
<br><br>
**with that we get a shell**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/shell.png)
<br><br>
**flag 2 found**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/flag2.png)
<br><br>
**searching around, file date stands out in wordpress directory**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/wpdate.png)
<br><br>
**wordpress config reveals db password**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/wpconfig.png)
<br><br>
**trying same password for kuya works**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/kuya.png)
<br><br>
**flag 3 revealed**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/flag3.png)
<br><br>
**checking .bash_history we find some special commands**
<br>![alt text](../vulnhub/2018/kuya_1/imgs/bashhist.png)
<br><br>
**after some googling, an interesting find seems to work to read /etc/shadow**<br>
[https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/](https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/)
<br>![alt text](../vulnhub/2018/kuya_1/imgs/shadow.png)
<br><br>















