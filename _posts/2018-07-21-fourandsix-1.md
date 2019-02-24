---
layout: post
title:  "FourAndSix: 1"
excerpt: CTF by Fred Wemeijer
tags: [vulnhub, ctf, walkthrough]
---

# FourAndSix: 1

## Goal 
proof.txt ?

## Download 
[https://www.vulnhub.com/entry/fourandsix-1,236/](https://www.vulnhub.com/entry/fourandsix-1,236/)

## Walkthrough 
**nmap**
<br>![alt text](../vulnhub/FourAndSix_1/nmap.png)
<br><br>**seems an nfs share is available, can be mounted with a .img file inside**
<br>![alt text](../vulnhub/FourAndSix_1/rpc_nfs.png)
<br><br>**mounting .img file, several .png and .jpeg images exist**
<br>![alt text](../vulnhub/FourAndSix_1/usb_stick.png)
<br><br>**seem like all legit files, binwalk also found nothing**
<br>![alt text](../vulnhub/FourAndSix_1/hello.png)
<br><br>**after nothing else, tried mounting root of system...it was successful**
<br>![alt text](../vulnhub/FourAndSix_1/mount_root.png)
<br><br>**able to pull master.passwd file with root and user account hashes**
<br>![alt text](../vulnhub/FourAndSix_1/master_passwd_1.png)
![alt text](../vulnhub/FourAndSix_1/master_passwd_2.png)
<br><br>**found proof.txt in root folder**
<br>![alt text](../vulnhub/FourAndSix_1/root_proof.png)
<br><br>
