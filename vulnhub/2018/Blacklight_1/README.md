---
layout: page
title: Blacklight: 1
permalink: vulnhub/2018/Blacklight_1
---

## Goal
2 flags ***or*** 2 flags & root

????

idk, got both flags & root...after a ***couple*** of reboots :)

## Download
[https://www.vulnhub.com/entry/blacklight-1,242/](https://www.vulnhub.com/entry/blacklight-1,242/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**default 80**
<br>![alt text](imgs/default80.png)
<br><br>**default 80 continued**
<br>![alt text](imgs/default80_2.png)
<br><br>**dirb**
<br>![alt text](imgs/dirb.png)
<br><br>**robots.txt**
<br>![alt text](/imgs/robots.png)
<br><br>**flag 1 and hint**
<br>![alt text](/imgs/flag1.png)
<br><br>**console on port 9072; allows 2 commands and shuts down**
<br>![alt text](/imgs/console9072.png)
<br><br>***annoying***, **let the reboots begin**
<br>![alt text](/imgs/nmap_closed.png)
<br><br>**able to send command outputs to readable files from web**
<br>![alt text](/imgs/console_home_ps.png)
<br><br>**/home shows two interesting files, console.rb & flag2-inside.jpg**
<br>![alt text](/imgs/home_1.png)
![alt text](/imgs/home_2.png)
<br><br>**ps shows command to run ruby console**
<br>![alt text](/imgs/ps.png)
<br><br>**cp the flag2 image to be viewed via web**
<br>![alt text](/imgs/flag2_copy.png)
<br><br>**looks like we need to extract flag**
<br>![alt text](/imgs/flag2_inside.png)
<br><br>**after strings, hexedit, steghide didn't work, the tool to use was hinted to us all along 'outguess'
<br>flag2 is revealed**
<br>![alt text](/imgs/flag2.png)
<br><br>**wasn't sure if root was necessary or possible so did it anyways
<br>using [this](https://github.com/secjohn/ruby-shells) ruby shell i got root**
<br>![alt text](/imgs/reverse.png)







