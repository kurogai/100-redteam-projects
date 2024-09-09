# FTP Brute Forcer

## Overview

This Python script is designed to perform brute-force attacks on FTP servers [for 100 Red Team Projects for Pentesters and Network Managers
, number 17](https://github.com/kurogai/100-redteam-projects). It supports two main functionalities:
1. **Single User Brute Force**: Attempts to log in using a single username with a list of passwords.
2. **Multi User Brute Force**: Attempts to log in using a list of usernames with a list of passwords.

Additionally, the script can generate all possible passwords of a given length using ASCII letters and digits.

## Features

- **Brute Force for Single User**: Try all passwords for a given username.
- **Brute Force for Multiple Users**: Try all combinations of usernames and passwords.
- **Password Generation**: Generate all possible passwords of a specified length.
- **Flexible Input**: Read usernames and passwords from files.

## Requirements

- Python 3.x
- `ftplib` (included with Python standard library)
- `itertools` (included with Python standard library)
- `string` (included with Python standard library)

## Installation

No additional installation is required beyond Python itself.

## Usage

1. **Prepare Input Files**:
    - Create a file named `passwords.txt` with a list of passwords, one per line.
    - Create a file named `users.txt` with a list of usernames, one per line.

2. **Update Script Configuration**:
    - Edit the `server` variable in the `main()` function to specify the target FTP server.
    - Edit the `username` variable in the `main()` function if using the single user brute-force mode.

3. **Run the Script**:
    - Choose one of the following functions to call in the `main()` function:
        - `brute_force_ftp_single_user(server, username, password_list)`: Attempts to log in using the single username with passwords from `passwords.txt`.
        - `brute_force_ftp_multi_user(server, username_list, password_list)`: Attempts to log in using all usernames and passwords from `users.txt` and `passwords.txt`.
        - `brute_force_ftp_single_user(server, username, generate_all_passwords(length))`: Attempts to log in using the single username with all possible passwords of the specified length.
    - Uncomment the desired function call in the `main()` function and run the script.


3. **Run the Script**:
    ```
    python ftp_bruteforce.py
    ```

## Notes

- **Ethical Use**: Ensure you have explicit permission to perform brute-force testing on the target FTP server. Unauthorized access is illegal and unethical.
- **Performance**: Generating all possible passwords can be resource-intensive. Use with caution, especially for large character sets and lengths.

## License

This script is provided for educational purposes only. Use it responsibly and within the bounds of the law.
