# BSides Vancouver: 2018

## Goal
uid=0(root) gid=0(root) groups=0(root)

## Download
[https://www.vulnhub.com/entry/bsides-vancouver-2018-workshop,231/](https://www.vulnhub.com/entry/bsides-vancouver-2018-workshop,231/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**ftp allows anonymous access**
<br>![alt text](imgs/ftp.png)
<br><br>**downloadable lists shows possible user accounts**
<br>![alt text](imgs/users.png)
<br><br>**default webpage**
<br>![alt_text](imgs/default80.png)
<br><br>**dirb**
<br>![alt_text](imgs/dirb.png)
<br><br>**robots.txt**
<br>![alt_text](imgs/robots.png)
<br><br>**wordpress instance**
<br>![alt_text](imgs/backup_wordpress.png)
<br><br>**enumerate users using wpscan**
<br>![alt_text](imgs/wpscan_enumerate_1.png)
<br>![alt_text](imgs/wpscan_enumerate_2.png)
<br><br>**wfuzz password for john**
<br>![alt_text](imgs/wfuzz.png)
<br><br>**admin wordpress access granted using john**
<br>![alt_text](imgs/wordpress_admin.png)
<br><br>**add reverse shell to footer.php**
<br>![alt_text](imgs/wp_footer_reverse.png)
<br><br>**low privilege reverse shell**
<br>![alt_text](imgs/reverse_shell.png)
<br><br>**/etc/passwd confirms lists of users**
<br>![alt_text](imgs/passwd_1.png)
<br>![alt_text](imgs/passwd_2.png)
<br><br>**ssh config file shows all users except anne use a public key**
<br>![alt_text](imgs/sshd_config_1.png)
<br>![alt_text](imgs/sshd_config_2.png)
<br><br>**use hydra against ssh**
<br>![alt_text](imgs/hydra.png)
<br><br>**ssh as anne with found password**
<br>![alt_text](imgs/anne.png)
<br><br>**sudo gives root privileges & flag**
<br>![alt_text](imgs/root_flag.png)
