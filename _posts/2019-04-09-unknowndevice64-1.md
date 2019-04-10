---
layout: post
title:  "unknowndevice64: 1"
excerpt: boot2root by @unknowndevice64
tags: [vulnhub, boot2root, walkthrough]
---

## Goal #
root

## Download #
[https://www.vulnhub.com/entry/unknowndevice64-1,293/](https://www.vulnhub.com/entry/unknowndevice64-1,293/)

## Walkthrough #

**nmap**
<br>![alt text](../vulnhub/unknowndevice64_1/nmap.png)
<br><br>

**default 80**
<br>![alt text](../vulnhub/unknowndevice64_1/default80.png)
<br><br>

**default 80 source; commented out jpg**
<br>![alt text](../vulnhub/unknowndevice64_1/default_source.png)
<br><br>

**jpg is accessible**<br>
<br>![alt text](../vulnhub/unknowndevice64_1/key_hidden.png)
<br><br>

**download and try steghide; h1dd3n was password and reveals txt file with brainfuck**
<br>![alt text](../vulnhub/unknowndevice64_1/hidden_brain.png)
<br><br>

**decoded brainfuck is user/pass**
<br>![alt text](../vulnhub/unknowndevice64_1/brain_decode.png)
<br><br>

**login worked, but to a restricted shell**
<br>![alt text](../vulnhub/unknowndevice64_1/restricted_shell.png)
<br><br>

**able to get to vi; so we try escaping restriction**
<br>![alt text](../vulnhub/unknowndevice64_1/vi_cmd.png)
<br><br>

**escape worked**
<br>![alt text](../vulnhub/unknowndevice64_1/vi_shell.png)
<br><br>

**commands work with full path**
<br>![alt text](../vulnhub/unknowndevice64_1/cmds.png)
<br><br>

**sudo shows that we can run a program ud64sys with no password**
<br>![alt text](../vulnhub/unknowndevice64_1/sudo.png)
<br><br>

**looking at program it's strace**
<br>![alt text](../vulnhub/unknowndevice64_1/strace.png)
<br><br>

**quick google [here](https://bltsec.ninja/2017/12/23/penetration-testing-linux-local-privilege-escalation-dev-random-k2/) and we have root**
<br>![alt text](../vulnhub/unknowndevice64_1/strace_root.png)
<br><br>

**and we have flag**
<br>![alt text](../vulnhub/unknowndevice64_1/flag1.png)
![alt text](../vulnhub/unknowndevice64_1/flag2.png)

