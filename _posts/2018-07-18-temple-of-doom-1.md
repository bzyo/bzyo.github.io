---
layout: post
title:  "Temple of Doom: 1"
excerpt: CTF by @0katz
tags: [vulnhub, ctf, walkthrough]
---

# Temple of Doom: 1

## Goal
root

## Download 
[https://www.vulnhub.com/entry/temple-of-doom-1,243/](https://www.vulnhub.com/entry/temple-of-doom-1,243/)

## Walkthrough
**nmap**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/nmap.png)
<br><br>**default 666 page**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/default666.png)
<br><br>**refreshing the page we see express node.js with error**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/refresh_node.png)
<br><br>**burpe shows encoded cookie**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/burpe.png)
<br><br>**sending to decoder, it's passing username/token**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/burpe_decoder.png)
<br><br>**we find the error; a quote missing before Friday; adding and encoding again**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/burpe_encode.png)
<br><br>**sending updated cookie, page works and we're greated with the username**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/burpe_repeater.png)
<br><br>**after much searching, this [post](https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/) seems like node.js deserialization is the right track**<br>**as in the post, [nodejsshell](https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py) is used to create reverse shell**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/nodejsshell.png)
<br><br>**creating the payload as in the post, we then encode**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/burpe_nodejsshell.png)
<br><br>**using repeater, we get our reverse shell as user nodeadmin**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/reverse_shell1.png)
<br><br>**another user does exist, fireman**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/fire_node.png)
<br><br>**it's found that ss-manager is being run as fireman by root**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/ps_entries.png)
<br><br>**after some searching, this [post](https://github.com/shadowsocks/shadowsocks-libev/issues/1734) shows a bug and how to execute commands on ss-manager**<br>
**using this information, another reverse shell is created as user fireman**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/reverse_shell2.png)
<br><br>**we find that some commands using sudo can be run with no passwords**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/sudo_l.png)
<br><br>**after some searching, this [post](https://www.securusglobal.com/community/2014/03/17/how-i-got-root-with-sudo/) shows how to run commands with sudo and tcpdump**
<br>**using this information, a script is crafted for another reverse shell as root**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/reverse_shell3.png)
<br><br>**from here we get flag, game over**
<br>![alt text](../vulnhub/2018/Temple_of_Doom_1/imgs/root_flag.png)
<br><br>





