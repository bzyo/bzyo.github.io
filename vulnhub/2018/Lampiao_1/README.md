# Goal #
root

# Download #
https://www.vulnhub.com/entry/lampiao-1,249/

# Walkthrough #
**nmap**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/nmap.png)
<br><br>
**default 80, doesn't work**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/default80.png)
<br><br>
**default 80 via telnet**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/default80telnet.png)
<br><br>
**default 1898, looks like drupal**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/default1898.png)
<br><br>
**a post states node2 isn't working**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/firstarticle.png)
<br><br>
**node2 lists two files**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/node2.png)
<br><br>
**audio.m4a spells out "user tiago"**<br>
**qrc.png is a qr code and tells us to try harder**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/qrc.png)
<br><br>
**robots.txt lists out a lot**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/robots.png)
<br><br>
**after much searching, changelog.txt seems interesting...drupalgeddon**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/changelog.png)
<br><br>
**setup metasploit**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/msf_drupalgeddon.png)
<br><br>
**reverse shell**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/reverseshell.png)
<br><br>
**etc passwd shows user tiago**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/etcpasswd.png)
<br><br>
**quick lookup on drupal mysql settings location**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/defaultdrupal.png)
<br><br>
**checking default settings**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/defaultsettings.png)
<br><br>
**mysql settings revealed**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/mysql_settings.png)
<br><br>
**try ssh with found password; success**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/tiagossh.png)
<br><br>
**lots of enumeration and finally went back to os/kernel version...old**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/version.png)
<br><br>
**search for dirty cow sploits**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/searchsploit.png)
<br><br>
**chose this one for stabilitiy based on this [comment](https://github.com/dirtycow/dirtycow.github.io/issues/25#issuecomment-255852675) as it is added automatically**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/dirtycowexploit.png)
<br><br>
**download and compile sploit**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/exploitprep.png)
<br><br>
**run sploit and get new root password**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/exploitrun.png)
<br><br>
**elevate to root and cat flag**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Lampiao_1/imgs/root_flag.png)
<br><br>
















