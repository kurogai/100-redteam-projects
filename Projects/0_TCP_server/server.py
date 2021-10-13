import socket

serverAddressPort = ("127.0.0.1", 65432)

bytesToSend = b'Hey there! We received the message.'

# Creating a TCP/IP socket
TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding server socket to the port
TCPServerSocket.bind(serverAddressPort)
print("Server up and Listening")


# Listening for incoming messages

TCPServerSocket.listen(10)
msg, address = TCPServerSocket.accept()

while 1:
   datafromClient = msg.recv(1024)
   msg.sendall(datafromClient)

