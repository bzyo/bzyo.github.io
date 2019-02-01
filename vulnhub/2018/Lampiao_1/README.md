# Lampiao: 1

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/lampiao-1,249/](https://www.vulnhub.com/entry/lampiao-1,249/)

## Walkthrough #
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>
**default 80, doesn't work**
<br>![alt text](imgs/default80.png)
<br><br>
**default 80 via telnet**
<br>![alt text](imgs/default80telnet.png)
<br><br>
**default 1898, looks like drupal**
<br>![alt text](imgs/default1898.png)
<br><br>
**a post states node2 isn't working**
<br>![alt text](imgs/firstarticle.png)
<br><br>
**node2 lists two files**
<br>![alt text](imgs/node2.png)
<br><br>
**audio.m4a spells out "user tiago"**<br>
**qrc.png is a qr code and tells us to try harder**
<br>![alt text](imgs/qrc.png)
<br><br>
**robots.txt lists out a lot**
<br>![alt text](imgs/robots.png)
<br><br>
**after much searching, changelog.txt seems interesting...drupalgeddon**
<br>![alt text](imgs/changelog.png)
<br><br>
**setup metasploit**
<br>![alt text](imgs/msf_drupalgeddon.png)
<br><br>
**reverse shell**
<br>![alt text](imgs/reverseshell.png)
<br><br>
**etc passwd shows user tiago**
<br>![alt text](imgs/etcpasswd.png)
<br><br>
**quick lookup on drupal mysql settings location**
<br>![alt text](imgs/defaultdrupal.png)
<br><br>
**checking default settings**
<br>![alt text](imgs/defaultsettings.png)
<br><br>
**mysql settings revealed**
<br>![alt text](imgs/mysql_settings.png)
<br><br>
**try ssh with found password; success**
<br>![alt text](imgs/tiagossh.png)
<br><br>
**lots of enumeration and finally went back to os/kernel version...old**
<br>![alt text](imgs/version.png)
<br><br>
**search for dirty cow sploits**
<br>![alt text](imgs/searchsploit.png)
<br><br>
**chose this one for stabilitiy based on this [comment](https://github.com/dirtycow/dirtycow.github.io/issues/25#issuecomment-255852675) as it is added automatically**
<br>![alt text](imgs/dirtycowexploit.png)
<br><br>
**download and compile sploit**
<br>![alt text](imgs/exploitprep.png)
<br><br>
**run sploit and get new root password**
<br>![alt text](imgs/exploitrun.png)
<br><br>
**elevate to root and cat flag**
<br>![alt text](imgs/root_flag.png)
<br><br>
















