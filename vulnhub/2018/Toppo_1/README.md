# Toppo: 1

## Goal
root

## Download 
[https://www.vulnhub.com/entry/toppo-1,245/](https://www.vulnhub.com/entry/toppo-1,245/)

## Walkthrough 
nmap
<br>![alt text](imgs/nmap.png)
<br>
default 80 page
<br>![alt text](imgs/default80.png)
<br>
dirb
<br>![alt text](imgs/dirb.png)
<br>
admin page/directory
<br>![alt text](imgs/admin.png)
<br>
notes with password and assuming user is ted
<br>![alt text](imgs/notes.png)
<br>
ssh as ted works
<br>![alt text](imgs/ted.png)
<br>
running linux privilege checker per usual
<br>![alt text](imgs/privcheck1.png)
<br>
what's this? already root??
<br>![alt text](imgs/privcheck2.png)
<br>
downloaded a modified script to read /etc/shadow
<br>![alt text](imgs/python1.png)
<br>
running yields contents of /etc/shadow
<br>![alt text](imgs/python2.png)
<br>
using john the password is revealed
<br>![alt text](imgs/john.png)
<br>
ssh as root works and flag revealed
<br>![alt text](imgs/root_flag.png)
<br>
