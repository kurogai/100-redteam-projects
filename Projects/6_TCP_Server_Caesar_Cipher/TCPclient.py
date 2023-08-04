import socket
import threading
import sys

# checks whether sufficient arguments have been provided
if len(sys.argv) != 4:
    print ("Correct usage: script, IP address, port number, secret key")
    exit()

# Choosing Nickname
nickname = input("Choose your nickname: ")
 
# takes the first argument from command prompt as IP address
host = str(sys.argv[1])
 
# takes second argument from command prompt as port number
port = int(sys.argv[2])

# takes third argument from command prompt as Caesar cipher key
key = int(sys.argv[3])

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Encrypt a message
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - (ord('a') + key)) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - (ord('A') + key)) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext
    
# Decrypt a message
def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                try:
                    sender = message.split(":", 1)[0]
                    content = message.split(":", 1)[1]
                    decrypted_message = '{}: {}'.format(sender, decrypt(content, key))
                    print(decrypted_message)
                except:
                    print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        content = input('')
        encrypted_message = '{}: {}'.format(nickname, encrypt(content, key))
        client.send(encrypted_message.encode('utf-8'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()