---
layout: post
title:  "Vulnhub Walkthrough: SkyDog: 2016 - Catch Me If You Can"
excerpt: CTF by [@jamesbower](https://twitter.com/jamesbower)
---
# Skydog: 2016 - Catch Me If You Can

## Goal 
Capture all 8 flags in the form of flag{MD5 Hash}

## Download 
[https://www.vulnhub.com/entry/skydog-2016-catch-me-if-you-can,166/](https://www.vulnhub.com/entry/skydog-2016-catch-me-if-you-can,166/)

## Walkthrough (in order of when flag captured) 
**Initial nmap reveals a web server running on 80,443 and ssh on port 22222**
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/nmap.png)
<br><br>

Flag #2: Obscurity or Security?
Connecting to ssh over port 22222 the banner provides flag 2
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag02.png)
<br><br>

Flag{53c82eba31f6d416f331de9162ebe997}
Using findmyhash, MD5 hash reveals the hint encrypt

Flag #3: Be Careful Agent, Frank Has Been Known to Intercept Traffic Our Traffic.
Initial inspection of web site reveals flag 3 in the ssl certificate
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/sslflag3.png)
<br><br>

flag3{f82366a9ddc064585d54e3f78bde3221}
Using findmyhash, MD5 hash reveals the hint personnel

Flag #1: Don’t go Home Frank! There’s a Hex on Your House.
Running dirb against site shows the previous flag hint is a web directory, however it comes back a 403 forbidden error
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/dirb.png)
<br><br>

Browsing to the site gives the error “﻿ACCESS DENIED!!! You Do Not Appear To Be Coming From An FBI Workstation. Preparing Interrogation Room 1. Car Batteries Charging....”
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/403personnel.png)
<br><br>

Running the site through burp suite, the site map shows a directory oldIE and a file html5.js
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/burp002.png)
<br><br>
Browsing to the site reveals a comment of a long hex string
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/oldIE.png)
<br><br>

When the hex string is converted it reveals flag 1
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag1.png)
<br><br>

flag{7c0132070a0ef71d542663e9dc1f5dee} 
Using findmyhash, MD5 hash reveals the hint nmap

Flag #4: A Good Agent is Hard to Find.
Running the JavaScript code through jsbeautifier.org allows to view the code easier and reveals two interesting comments
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/js.png)
<br><br>

First comment indicates support for IE4 FBI Workstations, which is exact wording from 403 error from personnel web directory. Making use of the flag hint, adding the following user-agent in burp allows the personnel directory to be viewed and reveals flag 4 and an additional clue
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/agentie4.png)
<br><br>


flag{14e10d570047667f904261e6d08f520f} 
Using findmyhash, MD5 hash reveals the hint evidence

Flag #5: The Devil is in the Details - Or is it Dialogue? Either Way, if it’s Simple, Guessable, or Personal it Goes Against Best PracticesUsing the clue on the personnel page (new+flag) with the new decrypted flag (evidence), I tried browsing to the directory newevidence and was prompted with authentication required
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/newevidence001.png)
<br><br>


Looking at the proxy history, it shows basic authorization base64 encoding is being used which can be brute forced however there is no known username. This is where the second comment from the JavaScript comes into play as it shows the username format of firstname.lastname. Looking up Agent Hanratty’s first name on imdb shows it is Carl.

With a username to go on, burp suite intruder was setup as such
Payload Positions: 
Choose the base64 encoded string
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder01.png)
<br><br>

Payload Sets: 
Set payload type to custom iterator
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder02.png)
<br><br>

Payload Options: 
Set position one to be the username and add a colon separator
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder03.png)
<br><br>

Set position two for word lists (my usual are big & names)
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder4.png)
<br><br>

Payload Processing:
Add processing rule to base64 encode the payload
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder5.png)
<br><br>

Payload Encoding:
Be sure to remove the equal sign
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder6.png)
<br><br>

Now go grab some popcorn…and after some time a 301 status appears. 
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/intruder7.png)
<br><br>

After a quick base64 decode it shows the password is Grace
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/preflag5.png)
<br><br>

Using these credentials allows access to the web page which has three links.
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/newevidence002.png)
<br><br>

First link is to a text file revealing flag 5, second link is an image file and the third is a pdf file.
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag5.png)
<br><br>

flag{117c240d49f54096413dd64280399ea9}
Using findmyhash, MD5 hash reveals the hint panam

Flag 6: Where in the World is Frank?
Running binwalk against both image and pdf files shows that there is more to the image file
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/binwalk.png)
<br><br>

Using steghide requires a passphrase and going on the flag hint, testing with the last hash revealed was successful as the info option reveals that there is a flag text file embedded. 
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/preflag6.png)
<br><br>

The extracted text files reveals both the encoded and decoded flag 6 with an additional clue
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag6.png)
<br><br>

flag{d1e5146b171928731385eb7ea38c37b8}
Double checking decoded flag by using md5online.org, MD5 hash reveals the hint ILoveFrance

Flag 7: Frank Was Caught on Camera Cashing Checks and Yelling - I’m The Fastest Man Alive!Using the flag hint, Googling “I’m The Fastest Man Alive!” reveals the name Barry Allen. Googling that name with the movie title reveals that Frank Abagnale Jr refers to himself as this name to Agent Hanratty. With only two flags left and not using ssh, I tried various combinations of barry allen with the additional clue from flag 6. Finally using barryallen as the username gave unprivileged shell access.
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/preflag7.png)
<br><br>

Available files are a flag text files, which reveals flag 7, and an unknown file with a .data extension.
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag7.png)
<br><br>

flag{bd2f6a1d5242c962a05619c56fa47ba6}
Using findmyhash, MD5 hash reveals the hint theflash

Flag 8: Franks Lost His Mind or Maybe it’s His Memory. He’s Locked Himself Inside the Building. Find the Code to Unlock the Door Before He Gets Himself Killed!Having ssh access gives the ability to download the file via sftp. Once downloaded and upon further inspection the file shows that it’s a zip file
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/data001.png)
<br><br>

Unzipping the file expands it to a 1GB file, which shows that it’s a data file. 
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/data002.png)
<br><br>

Going on the flag hint of “Maybe it’s His Memory” I tried volatility and it reveals notepad.exe running at pid 268. Looking at the cmdline of the pid it shows that a file named code.txt is in use, which links back to the flag hint “Find the Code”. 
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/preflag8.png)
<br><br>
(pslist grepped for screenshot)

When looking at the notepad display it reveals another hex string and when decode reveals flag 8.
<br>![alt text](../vulnhub/SkyDog_2016-CatchMeIfYouCan/imgs/flag8.png)
<br><br>

flag{841dd3db29b0fbbd89c7b5be768cdc81}
Unfortunately there was no Google reference to a decoded MD5 hash