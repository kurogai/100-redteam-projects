import socket

# Declaring and initializing local ip address and port to be used
localIP, localPort  = "127.0.0.1", 65432

#creating a TCP/IP socket

TCPclientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCPclientSocket.connect((localIP, localPort))



clientMsg = input("Type your message for the server here: ")
data = bytes(clientMsg, "utf-8")

# send message to the server using TCP socket
print("Sending message to {0} port {1}".format(localIP, localPort))
TCPclientSocket.sendall(data)

#receiving reply from the server
dataFromServer = str(TCPclientSocket.recv(1024))
print("Message received from the server: ", str(dataFromServer))

