---
layout: post
title:  "BSides Vancouver: 2018"
excerpt: boot2root by @abatchy17
tags: [vulnhub, boot2root, walkthrough]
---

# BSides Vancouver: 2018

## Goal
uid=0(root) gid=0(root) groups=0(root)

## Download
[https://www.vulnhub.com/entry/bsides-vancouver-2018-workshop,231/](https://www.vulnhub.com/entry/bsides-vancouver-2018-workshop,231/)

## Walkthrough
**nmap**
<br>![alt text](../vulnhub/BSides-Vancouver_2018/nmap.png)
<br><br>**ftp allows anonymous access**
<br>![alt text](../vulnhub/BSides-Vancouver_2018/ftp.png)
<br><br>**downloadable lists shows possible user accounts**
<br>![alt text](../vulnhub/BSides-Vancouver_2018/users.png)
<br><br>**default webpage**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/default80.png)
<br><br>**dirb**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/dirb.png)
<br><br>**robots.txt**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/robots.png)
<br><br>**wordpress instance**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/backup_wordpress.png)
<br><br>**enumerate users using wpscan**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/wpscan_enumerate_1.png)
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/wpscan_enumerate_2.png)
<br><br>**wfuzz password for john**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/wfuzz.png)
<br><br>**admin wordpress access granted using john**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/wordpress_admin.png)
<br><br>**add reverse shell to footer.php**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/wp_footer_reverse.png)
<br><br>**low privilege reverse shell**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/reverse_shell.png)
<br><br>**/etc/passwd confirms lists of users**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/passwd_1.png)
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/passwd_2.png)
<br><br>**ssh config file shows all users except anne use a public key**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/sshd_config_1.png)
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/sshd_config_2.png)
<br><br>**use hydra against ssh**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/hydra.png)
<br><br>**ssh as anne with found password**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/anne.png)
<br><br>**sudo gives root privileges & flag**
<br>![alt_text](../vulnhub/BSides-Vancouver_2018/root_flag.png)
