# Goal #
root

# Download #
https://www.vulnhub.com/entry/toppo-1,245/

# Walkthrough #
nmap
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/nmap.png)
<br>
default 80 page
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/default80.png)
<br>
dirb
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/dirb.png)
<br>
admin page/directory
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/admin.png)
<br>
notes with password and assuming user is ted
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/notes.png)
<br>
ssh as ted works
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/ted.png)
<br>
running linux privilege checker per usual
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/privcheck1.png)
<br>
what's this? already root??
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/privcheck2.png)
<br>
downloaded a modified script to read /etc/shadow
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/python1.png)
<br>
running yields contents of /etc/shadow
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/python2.png)
<br>
using john the password is revealed
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/john.png)
<br>
ssh as root works and flag revealed
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Toppo_1/imgs/root_flag.png)
<br>
