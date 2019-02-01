# Goal #
proof.txt ?

# Download #
https://www.vulnhub.com/entry/fourandsix-1,236/

# Walkthrough #
**nmap**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/nmap.png)
<br><br>**seems an nfs share is available, can be mounted with a .img file inside**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/rpc_nfs.png)
<br><br>**mounting .img file, several .png and .jpeg images exist**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/usb_stick.png)
<br><br>**seem like all legit files, binwalk also found nothing**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/hello.png)
<br><br>**after nothing else, tried mounting root of system...it was successful**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/mount_root.png)
<br><br>**able to pull master.passwd file with root and user account hashes**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/master_passwd_1.png)
![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/master_passwd_2.png)
<br><br>**found proof.txt in root folder**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/FourAndSix_1/imgs/root_proof.png)
<br><br>
