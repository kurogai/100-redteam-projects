
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

Parent Project: https://github.com/kurogai/100-mitre-attack-projects

-------------------------------------------------------------------------------------------------------------------------------------------
Level 1 | Basic | Example
------------------------------------------------|------------------------------------------------|-----------------------------------------
[0] | TCP or UDP server just to receive messages | :heavy_check_mark:
[1] | TCP chat server | :heavy_check_mark:
[2] | UDP chat server | :heavy_check_mark:
[3] | Multi-threaded UDP or TCP chat server | :heavy_check_mark:
[4] | Server for file transfers | :heavy_check_mark:
[5] | Caesar Cipher tool | :heavy_check_mark:
[6] | TCP chat server -> The messages should be encoded with Caesar Cipher | :x:
[7] | ROT13 Cipher | :heavy_check_mark:
[8] | UDP Chat server -> The messages should be encoded with ROT13 Cipher | :x:
[9] | Remote command execution | :heavy_check_mark:
[10] | Recreate the Netcat tool | :heavy_check_mark:
-------------------------------------------------------------------------------------------------------------------------------------------
Level 2 | Essential | Example
------------------------------------------------|------------------------------------------------|-----------------------------------------
[11] | Simple port scanner | :heavy_check_mark:
[12] | Port scanner with OS fingerprint using TTL (Time To Live) | :heavy_check_mark: 
[13] | Port scanner with port footprint (HTTP? DNS? FTP? IRC?) | :x:
[14] | Simple Web Directory brute-forcer (Threaded) | :heavy_check_mark:
[15] | Recursive Web Directory brute-forcer (Threaded peer recursion) | :heavy_check_mark:
[16] | Web Login bruteforce tool | :x:
[17] | FTP Login bruteforce tool | :heavy_check_mark:
[18] | SSH Login bruteforce tool | :heavy_check_mark:
[19] | FTP User footprint | :x:
[20] | MYSQL User footprint | :x:
[21] | Simple Google Bot for web scan | :x:
[22] | Auto website comment bot | :x:
[23] | Auto website message bot | :x:
[24] | Web-scrapping using Regex | :x:
[25] | Bot to collect information about someone using Google / Bing / Yahoo! | :heavy_check_mark:
[26] | Simple SQLi tester | :x:
[27] | Simple XSS tester | :x:
[28] | Simple Wordpress brute-forcer | :x:
[29] | SQLi database retriever | :x:
[30] | Spam creator | :x:

-------------------------------------------------------------------------------------------------------------------------------------------
Level 3 | Advanced Network Attacks | Example
------------------------------------------------|-------------------------------------------|----------------------------------------------
[31] | Payload for reverse shell | :x:
[32] | Payload to capture screenshots | :x:
[33] | Implement a Botnet | :x:
[34] | Passive web scanner | :x:
[35] | ARP poisoning tool | :x:
[36] | Application that creates random shortcuts on screen | :x:
[37] | Application to encrypt a file | :heavy_check_mark:
[38] | Develop a Ransomware application | :x:
[39] | Spam Email sender | :x:
[40] | HTTP server for phishing | :x:
[41] | Honeypot creator | :x:
[42] | Application that connects to the Tor Network | :x:
[43] | IRC Server | :x:
[44] | Packet Capture tool | :x:

-------------------------------------------------------------------------------------------------------------------------------------------
Level 4 | Data analysis, payloads and more networking | Example
------------------------------------------------|------------------------------------------|-----------------------------------------------
[45] | Packet Data analysis | :x:
[46] | Packet image analysis with OpenCV | :x:
[47] | Develop a hexdump tool | ✔️
[48] | Payload that moves the mouse cursor | :x:
[49] | Vigenère Cipher | :x:
[50] | Payload that starts automatically using Windows Regedit | :x:
[51] | Payload that starts as a daemon | :x:
[52] | Payload that retrieves browser information | :x:
[53] | Link generator | :x:
[54] | ASCII Name generator [ just for fun :) ]  | :x:
[55] | Full chat server with private messages, file and image transfer | :x:
[56] | Simple firewall | :x:
[57] | Gateway | :x:
[58] | Powershell payload generator | :x:
[59] | Bash payload generator | :x:
[60] | Subdomain enumerator | :x:
[61] | DNS Enumerator | :x:
[62] | Your own interpreter | :x:
[63] | Develop a Worm | :x:
[64] | Server for DDOS | :x:
[65] | Implement an IP Tracker | :x:
[66] | BurpSuite extender | :x:
[67] | Develop a Trojan | :x:
[68] | Man In The Browser tool (kind of) | :x:
[69] | Process monitor (Windows and Linux) | :x:
[70] | Windows token privilege escalation tool | :x:

-------------------------------------------------------------------------------------------------------------------------------------------
 Level 5 | Cryptography, Reverse Engineering and Post exploitation | Example
------------------------------------------------|------------------------------------------|-----------------------------------------------
[71] | Develop a code injection tool | :x:
[72] | Develop a Worm with auto replication over email | :x:
[73] | Simple Disassembler | :x:
[74] | Server for DDoS with multi-staged operations and multi-threaded handling of clients | :x:
[75] | Password hash cracker | :heavy_check_mark:
[76] | Direct code injection exploit | :x:
[77] | Android daemon payload | :x:
[78] | Browser exploitation tool | :x:
[79] | Simple tool for Reverse Engineering | :x:
[80] | Script for OS enumeration (after shell) | :x:
[81] | RSA Payload generator | :x:
[82] | Handshake capture | :x:
[83] | Wifi monitor | :x:
[84] | Buffer Overflow exploit | :x:
[85] | Stack Overflow exploit | :x:
[86] | Banner exploit | :x:
[87] | ISS Exploit | :x:
[88] | Wifi de-authentication attack (DoS) tool | :x:
[89] | Badchar detector | :x:
[90] | Firewall detector | :x:
[91] | Exploitation Framework | :x:
[92] | Botnet with SSH C&C and automatic server backup to prevent loss of control | :x:
[93] | Windows enumeration tool | :x:
[94] | Application information gathering (after shell) | :x:
[95] | Recreate TCPDUMP | :x:
[96] | Bluetooth exploit | :x:
[97] | Windows Blue Screen Exploit | :x:
[98] | Encoded exploit | :x:
[99] | Antivirus evasion application | :x:
[100] | Your own metasploit module | :x:

---

## Honorable Mentions:
- Kernel Mode rootkit: [reveng_rtkit](https://github.com/reveng007/reveng_rtkit) by [@reveng007](https://twitter.com/reveng007)

## Adding Your Examples:

You can make a pull request for the "Projects" directory and name the file in 
compliance with the following convention:

```
[ID] PROJECT_NAME - <LANGUAGE> | AUTHOR
```

#### Example:

```
[91] Web Exploitation Framework - <C> | EONRaider
```

### Want to support my work?
[<a href="https://www.buymeacoffee.com/heberjuliok" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>](https://www.buymeacoffee.com/heberjuliok)
