---
layout: post
title:  "unknowndevice64: 2"
excerpt: boot2root by @unknowndevice64
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/unknowndevice64-2,297/](https://www.vulnhub.com/entry/unknowndevice64-2,297/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/unknowndevice64_2/nmap.png)
<br><br>

**ran detailed nmap for unknown ports**
<br>![alt text](../vulnhub/unknowndevice64_2/nmap-detail.png)
<br><br>

**knowing this is android with debug port 5555 open, we get root and flag quickly by using adb to connect and get shell**
<br>![alt text](../vulnhub/unknowndevice64_2/root_flag.png)
<br><br>

**second way to get root we try through web interface on port 12345**<br><br>

**authentication required and it was a lot of trial and error**<br>
<br>![alt text](../vulnhub/unknowndevice64_2/webauth.png)
<br><br>

**not elegant, but manually tried some very default username/password combos.  turns out to be administrator/password**
<br>![alt text](../vulnhub/unknowndevice64_2/default12345.png)
<br><br>

**before doing automated enumeration we try robots.txt and it's there**
<br>![alt text](../vulnhub/unknowndevice64_2/robots.png)
<br><br>

**going to info.php prompts a download**
<br>![alt text](../vulnhub/unknowndevice64_2/infophp.png)
<br><br>

**turns out to be a private ssh key with a comment, most likley key password**
<br>![alt text](../vulnhub/unknowndevice64_2/infophp_key.png)
<br><br>

**echo the key into a file and change permissions**
<br>![alt text](../vulnhub/unknowndevice64_2/keyfile.png)
<br><br>

**ssh using key and password, success**
<br>![alt text](../vulnhub/unknowndevice64_2/ssh.png)
<br><br>

**we know root doesn't have a password and location of the flag, done**
<br>![alt text](../vulnhub/unknowndevice64_2/root_flag_ssh.png)
<br><br>
