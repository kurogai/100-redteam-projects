import socket
import threading
import queue
import string



messages = queue.Queue()
clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost",9999))

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


def receive():
    
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass

def broadcast():
    print("UDP server up and listening")
    while True:
        while messages.empty():
            message, addr = messages.get()
            print(message.decode())
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        name = message.decode()[message.decode().index(":")+1:]
                        server.sendto(rot13(f"{name} joined!").encode(), client)
                    else:
                        server.sendto(message, client)
                except Exception as e:
                    print(str(e))
                    clients.remove(client)


t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)


t1.start()
t2.start()
