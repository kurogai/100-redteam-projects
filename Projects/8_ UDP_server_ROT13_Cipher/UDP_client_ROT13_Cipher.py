import socket
import threading
import random
import queue
import string

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000, 9000)))
name = input ("Nickname: ")

def translator():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    shift = 13

    shift_lowercase = lowercase[shift:] + lowercase[:shift]
    shift_uppercase = uppercase[shift:] + uppercase[:shift]

    translate = str.maketrans(lowercase +uppercase, shift_lowercase + shift_uppercase)
    return translate

def rot13(message):
    table = translator()
    return message.translate(table)


def recieve():
    while True:
        try:
            message, _ = client.recvfrom(1024)
        
            encripted_message = message.decode()
            decrpted_message = rot13(encripted_message)
            print(decrpted_message)
        except:
            pass

t = threading.Thread(target=recieve)
t.start() 

client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 9999))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        encripted_message = rot13(message)
        client.sendto(rot13(f"{name}: {message}").encode(), ("localhost", 9999))

