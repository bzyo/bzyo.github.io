# Goal
4 flags / root

# Download
https://www.vulnhub.com/entry/raven-1,256/

# Walkthrough
**nmap**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/nmap.png)
<br><br>
**detailed nmap**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/nmap-detail.png)
<br><br>
**tested rpc but nothing there**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/showmount.png)
<br><br>
**dirb shows wordpress**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/dirb.png)
<br><br>
**found this out after the fact, had to add raven.local to hosts file for wp**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/hostsfile.png)
<br><br>
**default wp**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/defaultwp.png)
<br><br>
**wpscan enum finds two users**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/wpenum1.png)
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/wpenum2.png)
<br>
**wpscan brute finds nothing; huge rabbit hole**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/wpbrute1.png)
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/wpbrute2.png)
<br><br>
**only port left is ssh; tried hydra and creds found**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/hydra.png)
<br><br>
**ssh as michael**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/sshmichael.png)
<br><br>
**check etc/passwd; another user steven**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/etcpasswd.png)
<br><br>
**check wp-config; find mysql root creds**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/wpconfig.png)
<br><br>
**grab hash for steven**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/mysql.png)
<br><br>
**run against john; find pass**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/john_steven.png)
<br><br>
**elevate to steven; see that sudo python available; i am root**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/sudopython.png)
<br><br>
**root errr flag 4; lolz forgot i was looking for flags :P**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/flag4.png)
<br><br>
**searched for remaining 3 flags and found**
<br>**flag 1 was in service.html**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/flag1.png)
<br><br>**flag 2 was in /var/www**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/flag2.png)
<br><br>**flag 3 was in mysql or maybe a post?**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/flag3_1.png)
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Raven_1/imgs/flag3_2.png)
