---
layout: post
title:  "Wallaby's: Nightmare v1.0.2"
excerpt: CTF by waldo
tags: [vulnhub, boot2root, walkthrough]
---

## Goal
uid=0(root) gid=0(root) groups=0(root)

## Download 
[https://www.vulnhub.com/entry/wallabys-nightmare-102,176/](https://www.vulnhub.com/entry/wallabys-nightmare-102,176/)

## Walkthrough 
Initial nmap shows ssh on 22, web on 80, and closed irc on 6667
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-initialnmap.png)
<br><br>

Looking at the website and we need to enter a username to get started
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-80.png)
<br><br>

Username was just to personalize, now some tips and off we go
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-start.png)
<br><br>

Told we're being observed, but we now have a path to use /?page=
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-observe.png)
<br><br>

Throwing the site at dirb yields some interesting results. Almost too interesting...
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-initialdirb.png)
<br><br>

Going back to the website to check these results and it seems port 80 doesn't work anymore
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-dirbbroke.png)
<br><br>

Another nmap shows that 80 moved to 60080
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-nmapsecond.png)
<br><br>

Back to the website on the new port 60080 and greeted with a new message
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-60080initial.png)
<br><br>

Running dirb against the site on the new port yields same results
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-dirb60080.png)
<br><br>

Throwing nikto at the website reveals a possible way to read /etc/passwd
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-nikto.png)
<br><br>
*snippet of nikto results

While all the results from nikto seem to reveal the passwd file...
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-fakepasswd.png)
<br><br>

Looking at the source it's safe to assume it's fake
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-fakepasswdsource.png)
<br><br>

Back to the dirb results, it seems most of them are just fake as it throws an already patched message
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-vectorpatched.png)
<br><br>

The contact page works, but shows nothing much and neither does the source
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-contact.png)
<br><br>

The mailer page works also and doesn't show much...
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-mailer.png)
<br><br>

However the source of the mailer page reveals a new path to work with /?page=mailer&mail=mail wallaby "message goes here"
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-mailersource.png)
<br><br>

After some time of messing with the path, it turns out we have LFI
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-lfi.png)
<br><br>

Seems wget is working, so a reverse php shell is setup and ready to download
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wget.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-reversephp.png)
<br><br>

However after running it doesn't seem to download as there is no data in the file
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wgetfail.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-nodatareverse.png)
<br><br>

Looking at the access.log it seems to pull, but gets a 500 error
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-accesslog.png)
<br><br>

After some trial and error seems we need to chmod 777 the file and remove the .php extension in order for it to work
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-chmodreverse.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallabys-reversewgetnoext.png)
<br><br>

File is now showing data
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wgetworking.png)
<br><br>

Before we can get a shell we need to remove the old no data reverse.php file and copy the reverse file to include .php extension
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-rmcpreverse.png)
<br><br>

After calling the reverse.php page we have a limited shell as www-data
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-limitedshell.png)
<br><br>

Showing the true passwd file we see there are 3 users; ircd, waldo, and wallaby
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-etcpasswd.png)
<br><br>

Now we know irc is running, but we're unable to interact with it. After some digging it's revealed through 'sudo -l' that all users have the ability to use iptables with no password. We also see waldo has the ability to run vim on a specific file, which we'll come back to later
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-sudowaldo.png)
<br><br>

Looking at iptables it does show port 6667 (ircd service) blocked to external users
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-sudoiptables.png)
<br><br>

So let's delete that entry
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-deleteiptables.png)
<br><br>

An nmap against port 6667 reveals the service is now open :)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-nmapirc.png)
<br><br>

We're now able to connect using irssi
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-irssi.png)
<br><br>

Through /list it's revealed that there is a channel #wallabyschat and joining shows two other users; waldo and wallabysbot
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wallabyschat.png)
<br><br>

Hitting a wall, I went back to see if there were any clues in the file system. Seems the home directories for all three users (ircd, waldo, and wallaby) were available.  Digging shows wallabysbot is using sopel, a python irc bot, with an interesting file run.py
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-runpy.png)
<br><br>

Unfamiliar with sopel, I did a little reading. Seems you can get the available commands by using .help
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-sopelhelp.png)
<br><br>

Commands are then listed in a private message and run is shown...interesting
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-helpcommands.png)
<br><br>

Running help on the command shows that I can do an 'ls' command, but doing so throws a message that I'm not waldo
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-runnotwaldo.png)
<br><br>

Attempt to change nick to waldo fails as it's already in use
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallayb-setnickfail.png)
<br><br>

Back to the limited shell, we see waldo has a session open on pid 770
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-whowaldo.png)
<br><br>

After some time I remember the additional 'sudo -l' entry for waldo
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wwwsudo.png)
<br><br>

So we can vim into a file which doesn't seem like much, but we can execute commands within vim using :!command
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallayb-vimcommandwaldo.png)
<br><br>

So we can run commands as waldo within vim, we need waldo off irc, and we know the specific pid for the irc process ...so let's start vim as waldo and issue :!kill 770
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-waldovim.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-kill770.png)
<br><br>

After killing pid 770 we check to make sure the irc process is gone
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-waldonomore.png)
<br><br>

We now change our nick in irssi to waldo with /nick waldo and with the ability to use .run we see that we're wallaby
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-nowimwallaby.png)
<br><br>

The .run command did not allow a lot, just one word commands with no options. However we're able to run scripts. Creaing a test script, I'm able to download using wget, make executable, and .run processes the file
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-testscript.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-testworkingwww.png)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-runtestfail.png)
<br><br>

The script shows that it failed, however it did run.  Knowing sopel uses python, I setup a python reverse shell...
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-pyreverse.png)
<br><br>

Download using wget and make executable
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wgetpyreverse.png)
<br><br>

Before running I setup my listener on 444 and after the comand '.run /tmp/pyreverse'...we have reverse shell as wallaby
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-wallabyreverse.png)
<br><br>

First thing I check is what I can run as sudo and it's everything with no password
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-sudoaswallaby.png)
<br><br>

The command 'sudo -i' gives me root and the flag.txt file :)
<br>![alt text](../vulnhub/Wallabys_Nightmare-v102/wallaby-boomroot.png)
<br><br>
