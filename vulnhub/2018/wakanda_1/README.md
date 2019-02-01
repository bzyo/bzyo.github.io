---
layout: post
title: wakanda: 1
---

## goal
3 flags / root

## download
[https://www.vulnhub.com/entry/wakanda-1,251/](https://www.vulnhub.com/entry/wakanda-1,251/)

## walkthrough
**nmap**
<br>![alt text](/imgs/nmap.png)
<br><br>
**nmap detailed; ssh on 3333**
<br>![alt text](/imgs/nmap-detailed.png)
<br><br>
**showmount gives nothing**
<br>![alt text](/imgs/showmount.png)
<br><br>
**dirb shows fake directories**
<br>![alt text](/imgs/dirb.png)
<br><br>
**also fake secret.txt :)**
<br>![alt text](/imgs/secretlolz.png)
<br><br>
**default 80**
<br>![alt text](/imgs/default80.png)
<br><br>
**source default 80 shows hidden code**
<br>![alt text](/imgs/sourcedefault80.png)
<br><br>
**hidden link is french version**
<br>![alt text](/imgs/default80fr.png)
<br><br>
**knew there was an LFI, but it def took me some time to find**<br>
**found a great [writeup](https://www.idontplaydarts.com/2011/02/using-php-filter-for-local-file-inclusion/) on php://filter for local file inclusion which worked**
<br>![alt text](/imgs/phpbase64encode.png)
<br><br>
**putting that same request to curl gives us an easier string to copy**
<br>![alt text](/imgs/curl.png)
<br><br>
**decoded gives password :)**
<br>![alt text](/imgs/burpdecode.png)
<br><br>
**with no username, trying the only one found on website works**
<br>![alt text](/imgs/sshmamadou.png)
<br><br>
**ssh into python; break out to shell with some commands**
<br>![alt text](/imgs/python2shell.png)
<br><br>
**flag 1 found**
<br>![alt text](/imgs/flag1.png)
<br><br>
**etc/passwd shows other user devops**
<br>![alt text](/imgs/passwd.png)
<br><br>
**per usual; move to /tmp and download python linux priv escalation script**<br>
**note the interesting test file found owned by devops with relatively current date/time**
<br>![alt text](/imgs/enum.png)
<br><br>
**searching the output for devops shows writeble file owned by devops in /srv**
<br>![alt text](/imgs/enum2.png)
<br><br>
**viewing file it's a script that wrote the test file in /tmp**<br>
**assumption is this file is called every x minutes**
<br>![alt text](/imgs/antivirus.png)
<br><br>
**update the script with a python reverse shell to our attacking machine**
<br>![alt text](/imgs/pyrev.png)
<br><br>
**nc listener on 443 is connected to after about 5 minutes as devops user**
<br>![alt text](/imgs/devopsrevshell.png)
<br><br>
**flag 2 is found**
<br>![alt text](/imgs/flag2.png)
<br><br>
**looking at sudo, pip can be run with no password**
<br>![alt text](/imgs/sudopip.png)
<br><br>
**familiar of this, looked up [fakepip code](https://github.com/0x00-0x00/FakePip), downloaded, and updated**<br>
**another listener was setup on attacking machine using port 444**
<br>![alt text](/imgs/fakepip.png)
<br><br>
**on victim machine download updated python fakepip script and execute**
<br>![alt text](/imgs/runfakepip.png)
<br><br>
**with listener setup on attacking machine, reverse shell connects and root access acquired**
<br>![alt text](/imgs/rootrevshell.png)
<br><br>
**root flag**
<br>![alt text](/imgs/rootflag.png)
<br><br>
