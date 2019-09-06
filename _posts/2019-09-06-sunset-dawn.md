---
layout: post
title:  "sunset: dawn"
excerpt: boot2root by @whitecr0w1
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/sunset-dawn,341/](https://www.vulnhub.com/entry/sunset-dawn,341/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/sunset_dawn/nmap.png)
<br><br>

**default 80...nothing**
<br>![alt text](../vulnhub/sunset_dawn/default80.png)
<br><br>

**dirb finds a log folder...only one is accessable**
<br>![alt text](../vulnhub/sunset_dawn/dirb.png)
<br>![alt text](../vulnhub/sunset_dawn/logs.png)
<br><br>

**log shows that some folders are being monitored**
<br>![alt text](../vulnhub/sunset_dawn/mgmtlog.png)
<br><br>

**enum4linux shows an interesting share and usernames**
<br>![alt text](../vulnhub/sunset_dawn/enum4linux1.png)
<br>![alt text](../vulnhub/sunset_dawn/enum4linux2.png)
<br>![alt text](../vulnhub/sunset_dawn/enum4linux3.png)
<br><br>

**connecting to smb share we can write to it**
<br>![alt text](../vulnhub/sunset_dawn/smb.png)
<br><br>

**got lost for some time as i couldn't find anything.  i rebooted the system and noticed the management.log grew in size...hmmmm**

**updated management log shows some processes are continually happening**
<br>![alt text](../vulnhub/sunset_dawn/mgmtlog_reboot.png)
<br><br>

**created reverse shell file named web-control since it was being referenced in the log. setup listener and we have low priv access**
<br>![alt text](../vulnhub/sunset_dawn/reverse.png)
<br><br>

**we can sudo sudo with no password...and we have root**
<br>![alt text](../vulnhub/sunset_dawn/sudo_root.png)
<br><br>

**and root flag**
<br>![alt text](../vulnhub/sunset_dawn/root_flag.png)
<br><br>
