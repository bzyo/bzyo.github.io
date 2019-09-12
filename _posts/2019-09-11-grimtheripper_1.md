---
layout: post
title:  "GrimTheRipper: 1"
excerpt: boot2root by Manish Chandra
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/grimtheripper-1,350/](https://www.vulnhub.com/entry/grimtheripper-1,350/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/GrimTheRipper_1/nmap.png)
<br><br>

**default 80**
<br>![alt text](../vulnhub/GrimTheRipper_1/default80.png)
<br><br>

**dirb**
<br>![alt text](../vulnhub/GrimTheRipper_1/dirb.png)
<br><br>

**robots shows index2**
<br>![alt text](../vulnhub/GrimTheRipper_1/robots.png)
<br><br>

**index2**
<br>![alt text](../vulnhub/GrimTheRipper_1/index2.png)
<br><br>

**source of index2 reveals a base64 string**
<br>![alt text](../vulnhub/GrimTheRipper_1/index2-source.png)
<br><br>

**decode twice to find new directory**
<br>![alt text](../vulnhub/GrimTheRipper_1/decode.png)
<br><br>

**new directory shows wordpress**
<br>![alt text](../vulnhub/GrimTheRipper_1/101dir.png)
<br>![alt text](../vulnhub/GrimTheRipper_1/wordpress.png)
<br><br>

**wpscan finds a lot of vulns but nothing to get access and one user admin**
<br>![alt text](../vulnhub/GrimTheRipper_1/wpscan_init1.png)
<br>![alt text](../vulnhub/GrimTheRipper_1/wpscan_init2.png)
<br><br>

**run wpscan brute with rockyou (i split rockyou to multiple files) and password found**
<br>![alt text](../vulnhub/GrimTheRipper_1/wpscan1.png)
<br>![alt text](../vulnhub/GrimTheRipper_1/wpscan2.png)
<br><br>

**all links on site direct to 127.0.0.1**
<br>![alt text](../vulnhub/GrimTheRipper_1/localhost.png)
<br><br>

**using target redirector from burpe, able to login**
<br>![alt text](../vulnhub/GrimTheRipper_1/target_redirector.png)
<br>![alt text](../vulnhub/GrimTheRipper_1/wordpressdash.png)
<br><br>

**adding php reverse shell to footer and calling site, reverse shell acquired**
<br>![alt text](../vulnhub/GrimTheRipper_1/footer.png)
<br>![alt text](../vulnhub/GrimTheRipper_1/revshell.png)
<br><br>

**wordpress is so old, so is the os. easily found kernel exploit**
<br>![alt text](../vulnhub/GrimTheRipper_1/exploitdb.png)
<br><br>

**sploit words, root.  no flag though :P**
<br>![alt text](../vulnhub/GrimTheRipper_1/sploit_root.png)
<br><br>
