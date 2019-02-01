# BTRSys: v2.1

## Download
[https://www.vulnhub.com/entry/btrsys-v21,196/](https://www.vulnhub.com/entry/btrsys-v21,196/)

## Goal 
uid=0(root) gid=0(root) groups=0(root)

## Walkthrough
Initial nmap reveals ports on 21, 22, and 80
<br>![alt text](imgs/btr2-nmap-000.png)
<br><br>

Nothing special on web page or in the source
<br>![alt text](imgs/btr2-web-001.png)
<br><br>

robots.txt reveals a wordpress instance
<br>![alt text](imgs/btr2-robots-002.png)
<br><br>

Crude implementation of wordpress and nothing special after some enumeration
<br>![alt text](imgs/btr2-wordpress-003.png)
<br><br>

Throwing it at wpscan it reveals an older version with lots of vulns, but I suspect it's a ruse
<br>![alt text](imgs/btr2-wordpressvuln-004.png)
<br><br>

Enumerating users we find btrisk and admin
<br>![alt text](imgs/btr2-enumwp-005.png)
<br><br>

Brute forcing admin using wpscan reveals admin is the password as well
<br>![alt text](imgs/btr2-wpbrute-006.png)
<br><br>

We're able to login to wordpress
<br>![alt text](imgs/btr2-wpadmin-008.png)
<br><br>

First thing is to get our php reverse shell into footer.php and haha! Someone already left one on the style.css page. Not sure if this was intentional or not...
<br>![alt text](imgs/btr2-leftovers-009.png)
<br><br>

After prepping netcat, we pull up the wordpress instance and we have a reverse shell and confirm username btrisk
<br>![alt text](imgs/btr2-reverse-010.png)
<br><br>

Couldn't find much on enumeration so I grab mysql root password from wp-config.php
<br>![alt text](imgs/btr2-wpconfig-011.png)
<br><br>

Next we dump the wordpress database using mysql oneliners revealing usernames and passwords
<br>![alt text](imgs/btr2-sql1liner-012.png)
<br>![alt text](imgs/btr2-sql1liner2-014.png)
<br>![alt text](imgs/btr2-sql1liner3-015.png)
<br><br>

We throw the hash for btrisk at findmyhash and a password is revealed
<br>![alt text](imgs/btr2-hash-016.png)
<br><br>

We're able to ssh using the username btrisk and the found password
<br>![alt text](imgs/btr2-btriskshell-017.png)
<br><br>

Simple sudo -i elevates us to root
<br>![alt text](imgs/btr2-root-018.png)
<br><br>