
import socket

localIP             = "127.0.0.1"
localPort           = 20001
bufferSize          = 1024
msgFromServer       = "Message received on UDP Client and sending it again: "

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    message, address = UDPServerSocket.recvfrom(bufferSize)

    print("\nMessage from Client:{0} \nClient IP Address:{1} \n".format(message.decode('UTF-8'),address))

    bytesTosend = msgFromServer + message.decode('UTF-8')
    # Sending a reply to client
    UDPServerSocket.sendto(str.encode(bytesTosend), address)