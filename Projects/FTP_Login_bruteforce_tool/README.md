# FTP Brute-Forcer

A simple Python-based brute-forcer tool designed to attempt to login to an FTP server using a list of passwords.

## Features

- Attempts to connect to the specified FTP server using a provided list of passwords.
- Provides colored output for better readability.
- Displays a banner with the tool and author information.
- Uses argparse for command-line argument parsing.

## Prerequisites

- Python 3.x

## Usage

```
python ftp_bruteforcer.py -t [TARGET_IP] -u [USERNAME] -p [PATH_TO_PASSWORD_LIST]
```

## Arguments

- `-t`, `--target`: IP address of the target FTP server. (Required)
- `-u`, `--user`: Username for which you want to brute-force the password. (Required)
- `-p`, `--password`: Path to the file containing a list of passwords to attempt (one password per line). (Required)

## Example

```
python ftp_bruteforcer.py -t 127.0.0.1 -u admin -p passwords.txt
```