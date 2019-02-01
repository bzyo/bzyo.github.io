# DerpNStink: 1 

## Goal
4 Flags / Root

## Download
[https://www.vulnhub.com/entry/derpnstink-1,221/](https://www.vulnhub.com/entry/derpnstink-1,221/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**default 80**
<br>![alt text](imgs/default80.png)
<br><br>**flag 1 found buried in source**
<br>![alt text](imgs/flag1.png)
<br><br>**ran dirb**
<br>![alt text](imgs/dirb.png)
<br><br>**/temporary had nothing**
<br>![alt text](imgs/temporary.png)
<br><br>**ran additional dirb against /php finding phpmyadmin**
<br>![alt text](imgs/dirb_php.png)
<br><br>**ran additional dirb against /weblog finding wordpress**
<br>![alt text](imgs/dirb_weblog.png)
<br><br>**/etc/hosts file needs to have dns entry added for any resolve**
<br>![alt text](imgs/etc_hosts.png)
<br><br>**wordpress site exists**
<br>![alt text](imgs/weblog_wordpress.png)
<br><br>**wordpress enumeration finds two users**
<br>![alt text](imgs/wpscan_enum.png)
<br>![alt text](imgs/wpscan_enum2.png)
<br><br>**admin user on wordpress password is found**
<br>![alt text](imgs/wpscan_admin.png)
<br>![alt text](imgs/wpscan_admin2.png)
<br><br>**admin is not really an admin though**
<br>![alt text](imgs/wpadmin_notadmin.png)
<br><br>**looking for a way to gain reverse shell, wpscan reveals slideshow upload plugin vuln**
<br>![alt text](imgs/wpscan_slideshow.png)
<br><br>**uploading reverse php gives low level reverse shell**
<br>![alt text](imgs/reverse_shell.png)
<br><br>**wp-config reveals root mysql**
<br>![alt text](imgs/phpmyadmin_root.png)
<br><br>**going back to phpmyadmin, 2nd wp account hash found**
<br>![alt text](imgs/phpmyadmin_passhash.png)
<br><br>**running against john reveals password**
<br>![alt text](imgs/john.png)
<br><br>**this gives admin level access to wp and flag 2**
<br>![alt text](imgs/flag2.png)
<br><br>**/home reveals two users**
<br>![alt text](imgs/home.png)
<br><br>**no other escalation options for these, trying same wp pass for stinky on ftp works**
<br>![alt text](imgs/ftp_stinky.png)
<br>![alt text](imgs/ftp_stinky1.png)
<br><br>**file name key.txt is found buried and is a private key**
<br>![alt text](imgs/ftp_key.png)
<br>![alt text](imgs/key.png)
<br><br>**using downloaded key file gives ssh access as stinky**
<br>![alt text](imgs/ssh_stinky.png)
<br><br>**flag 3 is found**
<br>![alt text](imgs/flag3.png)
<br><br>**pcap file found reveals mrderp password**
<br>![alt text](imgs/pcap.png)
<br><br>**su to mrderp is successful**
<br>![alt text](imgs/su_mrderp.png)
<br><br>**file found on root folder /support reveals pastebin link**
<br>![alt text](imgs/support.png)
<br><br>**link shows what commands mrderp can run as sudo**
<br>![alt text](imgs/pastebin.png)
<br><br>**sudo commands are verified**
<br>![alt text](imgs/pastebin_verify.png)
<br><br>**there is no binaries folder under mrderp home directory**
<br>![alt text](imgs/no_binaries.png)
<br><br>**from here we setup for root access by creating folder and a file named derpy that will call a shell**
<br>![alt text](imgs/setup_shell.png)
<br><br>**running derpy with sudo gives root access and last flag**
<br>![alt text](imgs/flag4_root.png)
