## Goal
/flag.txt

## Download
[https://www.vulnhub.com/entry/bob-101,226/](https://www.vulnhub.com/entry/bob-101,226/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**default 80 page under construction**
<br>![alt text](imgs/default80.png)
<br><br>**login page disabled**
<br>![alt text](imgs/login_disabled.png)
<br><br>**dirb reveals robots**
<br>![alt text](imgs/dirb.png)
<br><br>**robots reveals more**
<br>![alt text](imgs/robots.png)
<br><br>**note about web shell**
<br>![alt text](imgs/lat_memo.png)
<br><br>**web shell doesn't accept basic command**
<br>![alt text](imgs/web_shell_1.png)
<br><br>**accepts full path to command; passwords page revealed**
<br>![alt text](imgs/web_shell_2.png)
<br><br>**this page was removed by bob**
<br>![alt text](imgs/passwords.png)
<br><br>**bob has old copy**
<br>![alt text](imgs/bob_home.png)
<br><br>**user creds revealed**
<br>![alt text](imgs/old_passwords.png)
<br><br>**ssh as seb**
<br>![alt text](imgs/ssh_seb.png)
<br><br>**user elliot home directory with interesting file**
<br>![alt text](imgs/elliot_home.png)
<br><br>**interesting file reveals elliot password**
<br>![alt text](imgs/admin_is_dumb.png)
<br><br>**su elliot**
<br>![alt text](imgs/su_elliot.png)
<br><br>**user bob home directory with gpg encrypted login file**
<br>![alt text](imgs/login_file.png)
<br><br>**notes script buried in folders**
<br>![alt text](imgs/secret_notes_1.png)
<br><br>**notes script is random, except all capital laters spells HARPOCRATES**
<br>![alt text](imgs/secret_notes_2.png)
<br><br>**secret word used against gpg file; reveals bob password**
<br>![alt text](imgs/login_decrypted.png)
<br><br>**su bob**
<br>![alt text](imgs/su_bob.png)
<br><br>**simple sudo gives root and flag revealed**
<br>![alt text](imgs/root_flag.png)







