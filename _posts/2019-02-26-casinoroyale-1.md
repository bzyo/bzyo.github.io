---
layout: post
title:  "Casino Royale: 1"
excerpt: CTF by @_creosote
tags: [vulnhub, ctf, walkthrough]
---

# Casino Royale: 1

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/casino-royale-1,287/](https://www.vulnhub.com/entry/casino-royale-1,287/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/CasinoRoyale_1/nmap.png)
<br><br>

**default 80**
<br>![alt text](../vulnhub/CasinoRoyale_1/default80.png)
<br><br>

**default 8081**
<br>![alt text](../vulnhub/CasinoRoyale_1/default8081.png)
<br><br>

**nothing happens after post**
<br>![alt text](../vulnhub/CasinoRoyale_1/failed8081.png)
<br><br>

**dirb shows some interesting directors**
<br>![alt text](../vulnhub/CasinoRoyale_1/dirb.png)
<br><br>

**cards...nothing**
<br>![alt text](../vulnhub/CasinoRoyale_1/cards.png)
<br><br>

**kboard...nothing**
<br>![alt text](../vulnhub/CasinoRoyale_1/kboard.png)
<br><br>

**robots is cards and kboard...lol**
<br>![alt text](../vulnhub/CasinoRoyale_1/robots.png)
<br><br>

**trying index.php reveals a pokermax software**
<br>![alt text](../vulnhub/CasinoRoyale_1/indexphp.png)
<br><br>

**we find an admin page, but default checks don't work**
<br>![alt text](../vulnhub/CasinoRoyale_1/pokeradmin.png)
<br><br>

**we move to sqlmap**
<br>![alt text](../vulnhub/CasinoRoyale_1/sqlmap.png)
<br><br>

**sqlmap success and we find the admin password**
<br>![alt text](../vulnhub/CasinoRoyale_1/sqlmapdump.png)
<br><br>

**pokermax admin logged in**
<br>![alt text](../vulnhub/CasinoRoyale_1/pokermaxadmin-loggedin.png)
<br><br>

**looking around, user valenka has some info in the profile**
<br>![alt text](../vulnhub/CasinoRoyale_1/pokerplayer.png)
<br><br>

**update /etc/hosts and browse to url, it's a cms**
<br>![alt text](../vulnhub/CasinoRoyale_1/snowfoxcms.png)
<br><br>

**going through the posts, this one looks interesting seeing how port 25 is open**
<br>![alt text](../vulnhub/CasinoRoyale_1/newclientpost.png)
<br><br> 

**quick search on e-db reveals a csrf attack that looks like it could work**
[https://www.exploit-db.com/exploits/35301](https://www.exploit-db.com/exploits/35301)

**setup the crsf file and hosted on attacking machine through apache**
<br>![alt text](../vulnhub/CasinoRoyale_1/snowfoxcsrf.png)
<br><br>

**setup for the email took some time trying to figure out the correct subject line, had to go one by one through the poker clients**
<br>![alt text](../vulnhub/CasinoRoyale_1/pokerclients.png)
<br><br>

**final send email with a link to the crsf file**
<br>![alt text](../vulnhub/CasinoRoyale_1/sendemail.png)
<br><br>

**access log shows file is checked!**
<br>![alt text](../vulnhub/CasinoRoyale_1/accesslog.png)
<br><br>

**attempt to sign-in with creds provided in crsf file**
<br>![alt text](../vulnhub/CasinoRoyale_1/signin1.png)
<br><br>

**success! in as admin**
<br>![alt text](../vulnhub/CasinoRoyale_1/signin2.png)
<br><br>

**wasted a lot of time looking for places to add php code, ends up there were details in a user profile again**
<br>![alt text](../vulnhub/CasinoRoyale_1/updateuseracct.png)
<br><br>

**browsing to the new url, it's a file directoy**
<br>![alt text](../vulnhub/CasinoRoyale_1/ultra.png)
<br><br>

**browring to main.php, nothing special**
<br>![alt text](../vulnhub/CasinoRoyale_1/ultra-main.png)
<br><br>

**but we find interesting notes in the source**
<br>![alt text](../vulnhub/CasinoRoyale_1/ultra-source.png

**looks like xxe vuln and here is a good post to follow**
[
https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection](
https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection)

**setup xml.txt and curl command**
<br>![alt text](../vulnhub/CasinoRoyale_1/xxe-setup.png)
<br><br>

**running reveals /etc/passwd**
<br>![alt text](../vulnhub/CasinoRoyale_1/xxe-success.png)
<br><br>

**now we have users, know that ftp is open and from the comment in the ultra source that it's an easy password.  through hydra at it...success**
<br>![alt text](../vulnhub/CasinoRoyale_1/ftppass.png)
<br><br>

**ftp access is successful, however we cannot do much. cannot upload, but can make directories**
<br>![alt text](../vulnhub/CasinoRoyale_1/ftpdenied.png)
<br><br>

**after some playing around, we can upload just without extensions :)**
<br>![alt text](../vulnhub/CasinoRoyale_1/ftpnoext.png)
<br><br>

**however we cannot add .php extension, but .php5 worked**
<br>![alt text](../vulnhub/CasinoRoyale_1/ftpphp5.png)
<br><br>

**we setup our netcat listener and browse to the file, but nothing happens. looking we need to add permissions to the file, we just 777 it**
<br>![alt text](../vulnhub/CasinoRoyale_1/ftpchmod.png)
<br><br>

**we revisit the file in the browser and we have a reverse shell**
<br>![alt text](../vulnhub/CasinoRoyale_1/revshell.png)
<br><br>

**quickly find valenka password for mysql**
<br>![alt text](../vulnhub/CasinoRoyale_1/valenkamysql.png)
<br><br>

**able to elevate to user valenka after breaking out of jail. after much searching, elevation didn't help though**
<br>![alt text](../vulnhub/CasinoRoyale_1/valenkasu.png)
<br><br>

**back as www-data, searched and found an interesting suid file and directory**
<br>![alt text](../vulnhub/CasinoRoyale_1/suid.png)
<br><br>

**running the suid file it seems it's pulling network stats and processes, most likely using run.sh**
<br>![alt text](../vulnhub/CasinoRoyale_1/mi6.png)
<br><br>

**from here we need to become user le, so we look at some of the servered by the webserver. it shows index.html calls collect.php**
<br>![alt text](../vulnhub/CasinoRoyale_1/indexcollect.png)
<br><br>

**we see it's calling the python script and we see it's editable by www-data. it's currently reading a log file, but perhaps we can change that to a reverse shell?**
<br>![alt text](../vulnhub/CasinoRoyale_1/datapy.png)
<br><br>

**we know we can access these files via that 8081 port. looking more closely we see that the web server at this port is run by user le**
<br>![alt text](../vulnhub/CasinoRoyale_1/phple.png)
<br><br>

**first let's create the new python script containing our reverse shell**
<br>![alt text](../vulnhub/CasinoRoyale_1/wwwle.png)
<br><br>

**next we download the file to /tmp**
<br>![alt text](../vulnhub/CasinoRoyale_1/wget.png)
<br><br>

**then we echo that file into the existing python script and overwrite the contents. we do a cat to verfiy as well**
<br>![alt text](../vulnhub/CasinoRoyale_1/overwritepy.png)
<br><br>

**we setup a netcat listener on the new port, browse site and trigger the python script...we have a reverse shell as user le!!**
<br>![alt text](../vulnhub/CasinoRoyale_1/lereverse.png)
<br><br>

**so now back to the run.sh file, we take a look and we see it's just netstat and ps commands**
<br>![alt text](../vulnhub/CasinoRoyale_1/runsh.png)
<br><br>

**well we own the file, let's chmod and append a /bin/sh**
<br>![alt text](../vulnhub/CasinoRoyale_1/runshchmod.png)
<br><br>

**with that let's run mi6...and we root**
<br>![alt text](../vulnhub/CasinoRoyale_1/root.png)
<br><br>

**moving to /root/flag folder we see a script flag.sh, which when run tells us to open to a url**
<br>![alt text](../vulnhub/CasinoRoyale_1/rootflag1.png)
<br><br>

**nice**
<br>![alt text](../vulnhub/CasinoRoyale_1/rootflag2.png)
<br><br>











