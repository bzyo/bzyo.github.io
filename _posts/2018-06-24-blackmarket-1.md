---
layout: post
title:  "BlackMarket: 1"
excerpt: CTF by @Acebomber911
tags: [vulnhub, ctf, walkthrough]
---

# BlackMarket: 1

## Goal
Find 6 flags & 1 root flag

## Download
[https://www.vulnhub.com/entry/blackmarket-1,223/](https://www.vulnhub.com/entry/blackmarket-1,223/)

## Walkthrough
**nmap**
<br>![alt text](../vulnhub/BlackMarket_1/nmap.png)
<br><br>**default 80**
<br>![alt text](../vulnhub/BlackMarket_1/default80.png)
<br><br>**flag 1 - default 80 source**
<br>![alt text](../vulnhub/BlackMarket_1/flag1_source.png)
<br><br>**flag 1 txt, doesn't give much clue except jason bourne**
<br>![alt text](../vulnhub/BlackMarket_1/flag1_decrypt.png)
<br><br>**no sqli or wfuzz brute**
<br>![alt text](../vulnhub/BlackMarket_1/failed_login_80.png)
<br><br>**google failed login message**
<br>![alt text](../vulnhub/BlackMarket_1/google_login_failed.png)
<br><br>**found git repo with default creds**
<br>![alt text](../vulnhub/BlackMarket_1/github_pos.png)
<br><br>**login as supplier**
<br>![alt text](../vulnhub/BlackMarket_1/login_supplier.png)
<br><br>**sqli using sqlmap on add product**
<br>![alt text](../vulnhub/BlackMarket_1/sqli_addproduct.png)
<br>![alt text](../vulnhub/BlackMarket_1/sqli_addproduct2.png)
<br><br>**flag 3**
<br>![alt text](../vulnhub/BlackMarket_1/flag3.png)
<br><br>**sqlmap provides hashes for blackmarket**
<br>![alt text](../vulnhub/BlackMarket_1/sqli_markethashes.png)
<br><br>**admin md5 hash**
<br>![alt text](../vulnhub/BlackMarket_1/admin_market_decrypt.png)
<br><br>**admin login success, flag 4, and possible hint**
<br>![alt text](../vulnhub/BlackMarket_1/admin_market_login.png)
<br><br>**flag 4 txt, guess no need to spend more time on this webapp**
<br>![alt text](../vulnhub/BlackMarket_1/flag4_decrypt.png)
<br><br>**dirb finds squirrelmail**
<br>![alt text](../vulnhub/BlackMarket_1/dirb.png)
<br><br>**guessed that ????? was a hint as jbourne email password from previous flag4 pop-up**
<br>![alt text](../vulnhub/BlackMarket_1/squirrelmail_jbourne.png)
<br><br>**jbourne email access**
<br>![alt text](../vulnhub/BlackMarket_1/squirrelmail_jbourne1.png)
<br>![alt text](../vulnhub/BlackMarket_1/squirrelmail_jbourne2.png)
<br><br>**flag 5 and secret msg**
<br>![alt text](../vulnhub/BlackMarket_1/flag5_secret.png)
<br><br>**flag 5 txt, duh**
<br>![alt text](../vulnhub/BlackMarket_1/flag5_decrypt.png)
<br><br>**found how to decode guessing at first two words as 'Hi Dimitri'**
<br>**decoded letters were opposite alphabet letters from middle out**
<br>![alt text](../vulnhub/BlackMarket_1/decode_msg.png)
<br><br>**added all possible key words to common wordlist, but nothing was found**
<br>![alt text](../vulnhub/BlackMarket_1/add_keywords.png)
<br><br>**since things have been misspelled and we're looking for a 'workshop', added rule to john to append a-zA-Z0-9 to front and back of the word workshop, and then created a new wordlist**
<br>![alt text](../vulnhub/BlackMarket_1/john_rule.png)
<br>![alt text](../vulnhub/BlackMarket_1/workshop_list.png)
<br><br>**running dirb with new wordlist proves successful**
<br>![alt text](../vulnhub/BlackMarket_1/dirb_workshop.png)
<br><br>**vworkshop shows another cms**
<br>![alt text](../vulnhub/BlackMarket_1/vworkshop_80.png)
<br><br>**were looking for kgbbackdoor though and it's there, sorta**
<br>![alt text](../vulnhub/BlackMarket_1/kgbbackdoor_dir.png)
<br><br>**dirb using different extensions proves successful, first .txt and then .php**
<br>![alt text](../vulnhub/BlackMarket_1/dirb_workshop_txt.png)
<br>![alt text](../vulnhub/BlackMarket_1/dirb_workshop_php.png)
<br><br>**flag 6 found and were moving off of webapps**
<br>![alt text](../vulnhub/BlackMarket_1/flag6.png)
<br>![alt text](../vulnhub/BlackMarket_1/flag6_decrypt.png)
<br><br>**backdoor is there, just not working...yet**
<br>![alt text](../vulnhub/BlackMarket_1/backdoor_php.png)
<br>![alt text](../vulnhub/BlackMarket_1/backdoor_source.png)
<br><br>**remember we need PassPass.jpg to make it work and the image was there**
<br>![alt text](../vulnhub/BlackMarket_1/backdoor_jpg.png)
<br><br>**downloading the image and throwing it at strings yields a pass**
<br>![alt text](../vulnhub/BlackMarket_1/strings_passpass.png)
<br><br>**then decimal to hex and hex to ascii**
<br>![alt text](../vulnhub/BlackMarket_1/decimal_hex.png)
<br>![alt text](../vulnhub/BlackMarket_1/hex_ascii.png)
<br><br>**using found password, we have our backdoor**
<br>![alt text](../vulnhub/BlackMarket_1/backdoor_access.png)
<br><br>**me need shell to work**
<br>![alt text](../vulnhub/BlackMarket_1/reverse_shell.png)
<br><br>**interesting finds under home**
<br>![alt text](../vulnhub/BlackMarket_1/ls_home.png)
<br><br>**nicky reveals flag 2**
<br>![alt text](../vulnhub/BlackMarket_1/home_nicky.png)
<br>![alt text](../vulnhub/BlackMarket_1/flag2.png)
<br><br>**flag 2 reveals nothing important**
<br>![alt text](../vulnhub/BlackMarket_1/flag2_decrypt.png)
<br><br>**dimitri has a secret**
<br>![alt text](../vulnhub/BlackMarket_1/secret_dimitri.png)
<br><br>**using technique from [netsec](https://netsec.ws/?p=337) to spawn a tty shell, root access gained using su and an alternate spelling of dimitri's secret**
<br>![alt text](../vulnhub/BlackMarket_1/root.png)
<br><br>**root flag**
<br>![alt text](../vulnhub/BlackMarket_1/theend.png)
