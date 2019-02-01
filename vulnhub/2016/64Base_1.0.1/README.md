# Download #
https://www.vulnhub.com/entry/64base-101,173/

# Goal #
Capture all 6 flags in flag{base64encoded} format

# Walkthrough #
Initial nmap shows port on 22 (non-ssh), web server on 80, port on 4899 and ssh on 62964
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-nmap.png)
<br><br>
Browsing to the shows base64 clue right off the bat.
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-www.png)
<br><br>
Decoding the message reveals to look at source < was going to be next step anyways :)
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-wwwdecode.png)
<br><br>
Looking at the source reveals a long alpha-numeric string
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-source.png)
<br><br>
Sending string to burp suite decoder with initial decode as ascii-hex and then base64 reveals flag1
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag1.png)
<br><br>
flag1{NjRiYXNlOlRoMzUzQHIzTjBUZGFEcjAxRHpVQHJlTDAwSzFpbmc0Cg==}
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag1decode.png)
<br><br>
Decoding flag shows a username and password of 64base:Th353@r3N0TdaDr01DzU@reL00K1ing4

With nowhere else to go I fallback to dirb, but there is sooo many listings
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-dirb.png)
<br><br>
*snippet of dirb

I remember that the initial nmap revealed a robots.txt file and it's loooong
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-robots.png)
<br><br>
*snippet of robots.txt

I revert to burp and spider the site, then filter the site map for 4xx responses and find admin
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-sitemap.png)
<br><br>
admin page reveals a login, but the credentials revealed in flag1 do not work
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-adminlogin.png)
<br><br>
Nothing left to go on I try the two unknown ports...

port 22 doesn't respond to ssh and nc gives output, but no way in
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-nc22.png)
<br><br>
port 4899 gives output, but no way in as well
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-nc4899.png)
<br><br>
No options I go back to the website and find an interesting portion of the post page
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-post.png)
<br><br>
With all those folders in the robots.txt I figure there has to be something else.  Looking at the post page, I notice below the wanted image there is a stanza of "Only respond if you are a real Imperial-Class BountyHunter"

Looking through the site map I notice Imperial-class doesn't get any response like all the other fake directories
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-imperialclass001.png)
<br><br>
Browsing to the directory gives a 404...however
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-Imperial-classforbidden.png)
<br><br>
If we look at the stanza though, class is with a capital C...and changing it in the path reveals a page
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-capitalC.png)
<br><br>
Looking at the source it seems we have to add BountyHunter to our path
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-Imperialsource.png)
<br><br>
And now another login
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-bountyhunterlogin.png)
<br><br>
Looking at the source reveals nothing, but we have to POST to login.php
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-bountyhuntersource.png)
<br><br>
Browsing to login.php page changes the path adding index.php. Looking at that source reveals three more alphanumeric strings. Seems there is an index.html and index.php
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-bountyloginsource.png)
<br><br>
The strings on their own do nothing, but putting them all together through burp decoder reveals flag2
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag2.png)
<br><br>
flag2{aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj12Snd5dEZXQTh1QQo=}

Decoded flag gives no hints, but rather just a video of [darth vader burping](https://youtu.be/vJwytFWA8uA)...enjoy

At a dead end again, I go back to burp to see if I can't login to that BountyHunter. Looking at the request, it seems we're passing basic authentication already. Hmmm?
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-basicauthlogin.png)
<br><br>
I guess there was a hint after all...burp

Sending to burp repeater it becomes apparent that we're not sending a POST to login.php, but rather just a GET to index.php. Simply changing the file is enough and we have flag3
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag3.png)
<br><br>
flag3{NTNjcjN0NWgzNzcvSW1wZXJpYWwtQ2xhc3MvQm91bnR5SHVudGVyL2xvZ2luLnBocD9mPWV4ZWMmYz1pZAo=}

Decoding the flag reveals our 53cr3t5h377 path
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-secretshell.png)
<br><br>
Browsing to the path reveals what looks like a shell
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-secretshellexec.png)
<br><br>
Remembering back to the post page instructions, we need to use system and not exec.  This change reveals flag4
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag4.png)
<br><br>
flag4{NjRiYXNlOjY0YmFzZTVoMzc3Cg==}

Decoding the flag reveals more credentials...
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag4decoded.png)
<br><br>
Which do not work on the admin page, nor ssh on port 62964
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-sshtest.png)
<br><br>
So now begins trial and error as I find I'm very limited as to what can be done with this shell...

nc reveals grumpy cat
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-grumpycat.png)
<br><br>
ls with options works
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-ls.png)
<br><br>
From what I can tell the following commands work
ls (with options)
ls .. < only up one directory
nc < brings up grumpy cat
ps (with options)
locate < revealed using --help
base64 < revealed using --help
xxd < revealed using --help
id
whoami

Also able to pull up files listed from ls command...here is cat
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-catweb.png)
<br><br>
After again much keyboard bashing, locate, find and xargs are my saviors revealing flag5. Was able to browse entire file system, but ended up finding flag in the admin folder that I've been trying to get to since the beginning
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag5.png)
<br><br>
flag5{TG9vayBJbnNpZGUhIDpECg==}   

Decoding the flag states to look inside
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag5decode.png)
<br><br>
Using a combination of the commands, I tried obvious ways to read the file...with no luck

less response
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-less.png)
<br><br>
more response
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-more.png)
<br><br>
With no way to read the file, I remember we're able to read files in the BountyHunter directory and xargs allows to copy files. Adding locate admin | xargs find | grep flag | xargs cp -t . copies the flag file to BountyHunter directory
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-locatecopy.png)
<br><br>
And of course we're not able to view...
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-forbidden.png)
<br><br>
Looking at the permissions, it's only read 004
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-readonlyflag5.png)
<br><br>
Many tries my friends, many tries and I get the permissions changed. Needed to use all commands originally used. Final string locate BountyHunter | xargs find | grep flag | xargs chmod 777
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-777flag5.png)
<br><br>
File reveals an image
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-usetheforcepic.png)
<br><br>
Downloading the image and "looking inside" using exiftool reveals another long alphanumeric string
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-exif.png)
<br><br>
*snippet of exiftool output

Throwing the long string at burp decoder with initial decode as ascii-hex and then base64 reveals a private key. To get a file, I ran the string on command line to file with echo longstring | xxd -r -p | base64 -d > priv.key
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-privkey.png)
<br><br>
Now with a private key, I change the permissions and attempt ssh to host using key. Prompted with a passphrase, I try 'usetheforce' as in the picture...it works! revealing flag6
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-flag6.png)
<br><br>
flag6{NGU1NDZiMzI1YTQ0NTEzMjRlMzI0NTMxNTk1NDU1MzA0ZTU0NmI3YTRkNDQ1MTM1NGU0NDRkN2E0ZDU0NWE2OTRlNDQ2YjMwNGQ3YTRkMzU0ZDdhNDkzMTRmNTQ1NTM0NGU0NDZiMzM0ZTZhNTk3OTRlNDQ2MzdhNGY1NDVhNjg0ZTU0NmIzMTRlN2E2MzMzNGU3YTU5MzA1OTdhNWE2YjRlN2E2NzdhNGQ1NDU5Nzg0ZDdhNDkzMTRlNmE0ZDM0NGU2YTQ5MzA0ZTdhNTUzMjRlMzI0NTMyNGQ3YTYzMzU0ZDdhNTUzMzRmNTQ1NjY4NGU1NDYzMzA0ZTZhNjM3YTRlNDQ0ZDMyNGU3YTRlNmI0ZDMyNTE3NzU5NTE2ZjNkMGEK}

Challenge not over...

Decoding flag first through burp, then through command line for better screenshot reveals one last clue
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-luke.png)
<br><br>
Running revealed command shows ending credits
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2016/64Base_1.0.1/imgs/base64-welldone.png)
<br><br>
*snippet of ending credits
