# Reverse Shell Payload Generator

Generate reverse shell payloads with ease using this handy bash script.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Examples](#examples)
7. [Disclaimer](#disclaimer)
8. [Contribute](#contribute)

## Introduction

This tool is designed to quickly generate reverse shell payloads for various platforms and languages. Perfect for penetration testers, ethical hackers, and cybersecurity enthusiasts.

## Features

- Supports various payload types: Bash, Python, Netcat, and PHP.
- Automatic IP address detection from specific interfaces.
- Random port generation if not specified.
- Payload encoding options: base64 or URL.
- Option to launch a Netcat listener after generating the payload.

## Requirements

- Bash environment
- The corresponding software/tools for each payload (e.g., Netcat, Python).
- For URL encoding: Python 3

## Installation

```
cd bash-reverse-shell
chmod +x script_name.sh
```

###Usage
```
./script_name.sh [OPTIONS]
Where OPTIONS can be:


    -t, --type           Payload Type [python, netcat, bash, php].
    -i, --ip             Local IP.
    -p, --port           Local Port.
    -r, --run            Run Netcat Listener.
    -e, --encode         Encode The Payload [base64, url].
    -I, --interface      Get The IP From Specific Interface (Default: tun0).
    -h, --help           Prints The Help and Exit.

```

### Examples
Generate a bash payload with auto-detected IP from the eth0 interface and start a Netcat listener:

```
./script_name.sh -t bash -I eth0 -r
```
Generate a URL encoded Python payload with a specific IP and port:

```
./script_name.sh -t python -i 192.168.1.10 -p 4444 -e url
```
Disclaimer
Always ensure that you have the proper permissions and that it's legal to run reverse shells on your target. Misuse may lead to legal consequences. This tool is developed for educational purposes and should be used responsibly.

Contribute
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

