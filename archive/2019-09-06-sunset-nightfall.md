---
layout: post
title:  "sunset: nightfall"
excerpt: boot2root by @whitecr0w1
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/sunset-nightfall,355/](https://www.vulnhub.com/entry/sunset-nightfall,355/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/sunset_nightfall/nmap.png)
<br><br>

**default 80...nothing with dirb either so moved on to smb**
<br>![alt text](../vulnhub/sunset_nightfall/default80.png)
<br><br>

**enum4linux gives us usernames and nothing else**
<br>![alt text](../vulnhub/sunset_nightfall/e4l_1.png)
<br>![alt text](../vulnhub/sunset_nightfall/e4l_2.png)
<br>![alt text](../vulnhub/sunset_nightfall/e4l_3.png)
<br><br>

**ran hydra against ftp with more common user...creds**
<br>![alt text](../vulnhub/sunset_nightfall/hydra_ftp.png)
<br><br>

**ftp as user and we write files and create directories in the user's home folder...ssh**
<br>![alt text](../vulnhub/sunset_nightfall/ftp.png)
<br><br>

**create a pub/priv key and copy pub to authorized_keys file**
<br>![alt text](../vulnhub/sunset_nightfall/ssh_keygen.png)
<br><br>

**upload new file to .ssh folder using ftp**
<br>![alt text](../vulnhub/sunset_nightfall/up_authkeys.png)
<br><br>

**ssh as matt works**
<br>![alt text](../vulnhub/sunset_nightfall/ssh.png)
<br><br>

**found suid find file under top level scripts folder**
<br>![alt text](../vulnhub/sunset_nightfall/suid.png)
<br><br>

**able to reach user.txt file in other users home directory**
<br>![alt text](../vulnhub/sunset_nightfall/user.png)
<br><br>

**we create .ssh file and cp authorized_keys file over to other users home directory using this method**
<br>![alt text](../vulnhub/sunset_nightfall/find_cp.png)
<br><br>

**ssh as other user**
<br>![alt text](../vulnhub/sunset_nightfall/ssh_nightfall.png)
<br><br>

**grab root shadow hash**
<br>![alt text](../vulnhub/sunset_nightfall/sudo_shadow.png)
<br><br>

**run hash against hashcat**
<br>![alt text](../vulnhub/sunset_nightfall/hashcat.png)
<br><br>

**we have root**
<br>![alt text](../vulnhub/sunset_nightfall/root.png)
<br><br>

**and flag**
<br>![alt text](../vulnhub/sunset_nightfall/root_flag1.png)
<br>![alt text](../vulnhub/sunset_nightfall/root_flag2.png)
<br><br>