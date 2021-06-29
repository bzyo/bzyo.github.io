---
layout: post
title:  "bossplayersCTF: 1"
excerpt: ctf by Cuong Nguyen
tags: [vulnhub, ctf, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/bossplayersctf-1,375/](https://www.vulnhub.com/entry/bossplayersctf-1,375/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/bossplayersCTF_1/nmap.png)
<br><br>

**default 80**
<br>![alt text](../vulnhub/bossplayersCTF_1/default80.png)
<br><br>

**base64 comment revealed in source**
<br>![alt text](../vulnhub/bossplayersCTF_1/default80source.png)
<br><br>

**base64 decoded to site page**
<br>![alt text](../vulnhub/bossplayersCTF_1/base64.png)
<br><br>

**navigate to page and seems to point to rce**
<br>![alt text](../vulnhub/bossplayersCTF_1/workinginprogress.png)
<br><br>

**after testing various different words to trigger execution (command, ping, file)...cmd works**
<br>![alt text](../vulnhub/bossplayersCTF_1/cmd_id.png)
<br><br>

**reverse shell achieved**
<br>![alt text](../vulnhub/bossplayersCTF_1/reverse_shell.png)
<br><br>

**after some searching looks suid 'find' seems likely**
<br>![alt text](../vulnhub/bossplayersCTF_1/suid_find.png)
<br><br>

**root**
<br>![alt text](../vulnhub/bossplayersCTF_1/root.png)
<br><br>

**root flag**
<br>![alt text](../vulnhub/bossplayersCTF_1/root_flag.png)
<br><br>