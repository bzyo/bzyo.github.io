# JIS-CTF: VulnUpload

## Goal
Find 5 flags

## Download
[https://www.vulnhub.com/entry/jis-ctf-vulnupload,228/](https://www.vulnhub.com/entry/jis-ctf-vulnupload,228/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**dirb**
<br>![alt text](imgs/dirb.png)
<br><br>**login form**
<br>![alt text](imgs/login.png)
<br><br>**robots.txt reveals additional files/directories**
<br>![alt text](imgs/robots.png)
<br><br>**flag 1 found @ flag**
<br>![alt text](imgs/flag1.png)
<br><br>**flag 2 found in fake admin area source**
<br>![alt text](imgs/flag2.png)
<br><br>**use credentials found from flag 2 to login, area to upload files revealed**
<br>![alt text](imgs/login_successful.png)
<br><br>**able to upload reverse shell php file**
<br>![alt text](imgs/upload.png)
<br><br>**accessing uploaded php file under uploaded_files folder gives limited access shell**
<br>![alt text](imgs/reverse.png)
<br><br>**flag 3 found in hint.txt**
<br>![alt text](imgs/flag3.png)
<br><br>**flag 4 found in txt file buried in mysql directory**
<br>![alt text](imgs/flag4.png)
<br><br>**flag 5 found in flag.txt after using credentials to ssh as technawi**
<br>![alt text](imgs/flag5.png)
