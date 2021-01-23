
<p align="center"> 
    <img src="/images/red.png">
</p>
                                                                       
# 100  Red Team Projects for Pentesters and Network Managers

Red Teaming is one of the most attractive fields in offensive security or ethical hacking. 
Every day professionals and students are learning, creating and exploiting all types of 
systems. The internet is not only the most common means through which people interact 
and chat, but also a place where they are constantly exposed to a world where anyone can be monitored, 
exploited, tracked or scammed.

This is why us, programmers, take action; several of us continually try to protect this 
wonderful place while others, out of immaturity or shrewd interests, act in just the opposite direction. 
If you're interested in this field and want to join it, no matter your current level of knowledge, learning 
how to create your own tools will result in great advantage as a pentester.

So I put some thought into it and got the idea to create this project list aimed at anyone who is interested 
in learning "how to" not become the ultimate script kiddie. Here I discriminate (based solely on my own experience) 
almost 100 types of projects that you should at least try to either implement or study.

I recommend you to do them on the programming language you are most comfortable with. Implementing these 
projects will definitely help you gain more experience and, consequently, master the language. They are divided 
in categories, ranging from super basic to advanced projects.

If you enjoy this list please take the time to recommend it to a friend and follow me! I will be happy with that :)

And remember: With great power comes... (we already know).

---------------------------------------------------------------------------------------------
Level 1 | Basic
------------------------------------------------|--------------------------------------------
[0] | TCP or UDP server just to receive messages
[1] | TCP chat server
[2] | UDP chat server
[3] | Multi-threaded UDP or TCP chat server
[4] | Server for file transfers
[5] | Caesar Cipher tool
[6] | TCP chat server -> The messages should be encoded with Caesar Cipher
[7] | ROT13 Cipher
[8] | UDP Chat server -> The messages should be encoded with ROT13 Cipher
[9] | Remote command execution
[10] | Recreate the Netcat tool
--------------------------------------------------------------------------------------------
Level 2 | Essential
------------------------------------------------|-------------------------------------------
[11] | Simple port scanner
[12] | Port scanner with OS fingerprint using TTL (Time To Live)
[13] | Port scanner with port footprint (HTTP? DNS? FTP? IRC?)
[14] | Simple Web Directory brute-forcer (Threaded)
[15] | Recursive Web Directory brute-forcer (Threaded peer recursion)
[16] | Web Login bruteforce tool
[17] | FTP Login bruteforce tool
[18] | SSH Login bruteforce tool
[19] | FTP User footprint
[20] | MYSQL User footprint
[21] | Simple Google Bot for web scan
[22] | Auto website comment bot
[23] | Auto website message bot
[24] | Web-scrapping using Regex
[25] | Bot to collect information about someone using Google / Bing / Yahoo!
[26] | Simple SQLi tester
[27] | Simple XSS tester
[28] | Simple Wordpress brute-forcer
[29] | SQLi database retriever
[30] | Spam creator
--------------------------------------------------------------------------------------------
Level 3 | Advanced Network Attacks
------------------------------------------------|-------------------------------------------
[31] | Payload for reverse shell
[32] | Payload to capture screenshots
[33] | Implement a Botnet
[34] | Passive web scanner
[35] | ARP poisoning tool
[36] | Application that creates random shortcuts on screen
[37] | Application to encrypt a file
[38] | Develop a Ransomware application
[39] | Spam Email sender
[40] | HTTP server for phishing
[41] | Honeypot creator
[42] | Application that connects to the Tor Network
[43] | IRC Server
[44] | Packet Capture tool

-------------------------------------------------------------------------------------------
Level 4 | Data analysis, payloads and more networking
------------------------------------------------|------------------------------------------
[45] | Packet Data analysis
[46] | Packet image analysis with OpenCV
[47] | Develop a hexdump tool
[48] | Payload that moves the mouse cursor
[49] | Vigenère Cipher
[50] | Payload that starts automatically using Windows Regedit
[51] | Payload that starts as a daemon
[52] | Payload that retrieves browser information
[53] | Link generator
[54] | ASCII Name generator [ just for fun :) ] 
[55] | Full chat server with private messages, file and image transfer
[56] | Simple firewall
[57] | Gateway
[58] | Powershell payload generator
[59] | Bash payload generator
[60] | Subdomain enumerator
[61] | DNS Enumerator
[62] | Your own interpreter
[63] | Develop a Worm
[64] | Server for DDOS
[65] | Implement an IP Tracker
[66] | BurpSuite extender
[67] | Develop a Trojan
[68] | Man In The Browser tool (kind of)
[69] | Process monitor (Windows and Linux)
[70] | Windows token privilege escalation tool

------------------------------------------------------------------------------------------
 Level 5 | Cryptography, Reverse Engineering and Post exploitation
------------------------------------------------|------------------------------------------
[71] | Develop a code injection tool
[72] | Develop a Worm with auto replication over email
[73] | Simple Disassembler
[74] | Server for DDoS with multi-staged operations and multi-threaded handling of clients
[75] | Password hash cracker
[76] | Direct code injection exploit
[77] | Android daemon payload
[78] | Browser exploitation tool
[79] | Simple tool for Reverse Engineering
[80] | Script for OS enumeration (after shell)
[81] | RSA Payload generator
[82] | Handshake capture
[83] | Wifi monitor
[84] | Buffer Overflow exploit
[85] | Stack Overflow exploit
[86] | Banner exploit
[87] | ISS Exploit
[88] | Wifi de-authentication attack (DoS) tool
[89] | Badchar detector
[90] | Firewall detector
[91] | Exploitation Framework
[92] | Botnet with SSH C&C and automatic server backup to prevent loss of control
[93] | Windows enumeration tool
[94] | Application information gathering (after shell)
[95] | Recreate TCPDUMP
[96] | Bluetooth exploit
[97] | Windows Blue Screen Exploit
[98] | Encoded exploit
[99] | Antivirus evasion application
[100] | Your own metasploit module
------------------------------------------------------------------------------------------
## Adding your examples

You can make a pull request for the "Projects" directory and name the file in 
compliance with the following convention:

```
[ID] PROJECT_NAME - <LANGUAGE> | AUTHOR
```

#### Example:

```
[91] Web Exploitation Framework - <C> | EONRaider
```
