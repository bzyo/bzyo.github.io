# BlackMarket: 1

## Goal
Find 6 flags & 1 root flag

## Download
[https://www.vulnhub.com/entry/blackmarket-1,223/](https://www.vulnhub.com/entry/blackmarket-1,223/)

## Walkthrough
**nmap**
<br>![alt text](imgs/nmap.png)
<br><br>**default 80**
<br>![alt text](imgs/default80.png)
<br><br>**flag 1 - default 80 source**
<br>![alt text](imgs/flag1_source.png)
<br><br>**flag 1 txt, doesn't give much clue except jason bourne**
<br>![alt text](imgs/flag1_decrypt.png)
<br><br>**no sqli or wfuzz brute**
<br>![alt text](imgs/failed_login_80.png)
<br><br>**google failed login message**
<br>![alt text](imgs/google_login_failed.png)
<br><br>**found git repo with default creds**
<br>![alt text](imgs/github_pos.png)
<br><br>**login as supplier**
<br>![alt text](imgs/login_supplier.png)
<br><br>**sqli using sqlmap on add product**
<br>![alt text](imgs/sqli_addproduct.png)
<br>![alt text](imgs/sqli_addproduct2.png)
<br><br>**flag 3**
<br>![alt text](imgs/flag3.png)
<br><br>**sqlmap provides hashes for blackmarket**
<br>![alt text](imgs/sqli_markethashes.png)
<br><br>**admin md5 hash**
<br>![alt text](imgs/admin_market_decrypt.png)
<br><br>**admin login success, flag 4, and possible hint**
<br>![alt text](imgs/admin_market_login.png)
<br><br>**flag 4 txt, guess no need to spend more time on this webapp**
<br>![alt text](imgs/flag4_decrypt.png)
<br><br>**dirb finds squirrelmail**
<br>![alt text](imgs/dirb.png)
<br><br>**guessed that ????? was a hint as jbourne email password from previous flag4 pop-up**
<br>![alt text](imgs/squirrelmail_jbourne.png)
<br><br>**jbourne email access**
<br>![alt text](imgs/squirrelmail_jbourne1.png)
<br>![alt text](imgs/squirrelmail_jbourne2.png)
<br><br>**flag 5 and secret msg**
<br>![alt text](imgs/flag5_secret.png)
<br><br>**flag 5 txt, duh**
<br>![alt text](imgs/flag5_decrypt.png)
<br><br>**found how to decode guessing at first two words as 'Hi Dimitri'**
<br>**decoded letters were opposite alphabet letters from middle out**
<br>![alt text](imgs/decode_msg.png)
<br><br>**added all possible key words to common wordlist, but nothing was found**
<br>![alt text](imgs/add_keywords.png)
<br><br>**since things have been misspelled and we're looking for a 'workshop', added rule to john to append a-zA-Z0-9 to front and back of the word workshop, and then created a new wordlist**
<br>![alt text](imgs/john_rule.png)
<br>![alt text](imgs/workshop_list.png)
<br><br>**running dirb with new wordlist proves successful**
<br>![alt text](imgs/dirb_workshop.png)
<br><br>**vworkshop shows another cms**
<br>![alt text](imgs/vworkshop_80.png)
<br><br>**were looking for kgbbackdoor though and it's there, sorta**
<br>![alt text](imgs/kgbbackdoor_dir.png)
<br><br>**dirb using different extensions proves successful, first .txt and then .php**
<br>![alt text](imgs/dirb_workshop_txt.png)
<br>![alt text](imgs/dirb_workshop_php.png)
<br><br>**flag 6 found and were moving off of webapps**
<br>![alt text](imgs/flag6.png)
<br>![alt text](imgs/flag6_decrypt.png)
<br><br>**backdoor is there, just not working...yet**
<br>![alt text](imgs/backdoor_php.png)
<br>![alt text](imgs/backdoor_source.png)
<br><br>**remember we need PassPass.jpg to make it work and the image was there**
<br>![alt text](imgs/backdoor_jpg.png)
<br><br>**downloading the image and throwing it at strings yields a pass**
<br>![alt text](imgs/strings_passpass.png)
<br><br>**then decimal to hex and hex to ascii**
<br>![alt text](imgs/decimal_hex.png)
<br>![alt text](imgs/hex_ascii.png)
<br><br>**using found password, we have our backdoor**
<br>![alt text](imgs/backdoor_access.png)
<br><br>**me need shell to work**
<br>![alt text](imgs/reverse_shell.png)
<br><br>**interesting finds under home**
<br>![alt text](imgs/ls_home.png)
<br><br>**nicky reveals flag 2**
<br>![alt text](imgs/home_nicky.png)
<br>![alt text](imgs/flag2.png)
<br><br>**flag 2 reveals nothing important**
<br>![alt text](imgs/flag2_decrypt.png)
<br><br>**dimitri has a secret**
<br>![alt text](imgs/secret_dimitri.png)
<br><br>**using technique from [netsec](https://netsec.ws/?p=337) to spawn a tty shell, root access gained using su and an alternate spelling of dimitri's secret**
<br>![alt text](imgs/root.png)
<br><br>**root flag**
<br>![alt text](imgs/theend.png)
