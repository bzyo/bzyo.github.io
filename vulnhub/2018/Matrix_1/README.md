# Goal
root flag

# Download
https://www.vulnhub.com/entry/matrix-1,259/

# Walkthrough
**nmap**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/nmap.png)
<br><br>
**default 80**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/default80.png)
<br><br>
**default 31337**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/default31337.png)
<br><br>
**source 31337**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/source31337.png)
<br><br>
**decode string found in burp**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/decodeburp.png)
<br><br>
**guessed at using last part as a file name and it downloads**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/filedl.png)
<br><br>
**checking file, looks like brainfuck**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/filecheck.png)
<br><br>
**decoded gives partial password for guest**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/brainfuckdecode.png)
<br><br>
**wrote python script to generate random 2 characters and add to end of known password**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/guesspy.png)
<br><br>
**generated a text file with lots of possibilities and ran with hydra**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/generatehydra.png)
<br><br>
**ssh using found password; looks like a restricted shell**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/sshrestrict.png)
<br><br>
**tried the usual jail breaks, but failed**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/jailbreakfail.png)
<br><br>
**seems that vi jail break works but with limited commands**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/vibreakjail.png)
<br>
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/limitcmds.png)
<br><br>
**updated with a regular path and commands now work normally**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/pathupdate.png)
<br><br>
**see what sudo says; we can run all commands and get root lolz**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/sudo.png)
<br><br>
**root flag**
<br>![alt text](https://github.com/bzyo/vulnhub/blob/master/2018/Matrix_1/imgs/rootflag.png)
<br><br>
