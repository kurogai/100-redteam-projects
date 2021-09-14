import socket

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while True:
    msgFromClient       = input("Send Some text to UDP Server: ")
    bytesToSend         = str.encode(msgFromClient)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    message, address = UDPClientSocket.recvfrom(bufferSize)
    msg = "\nMessage from Server: {} \n".format(message.decode('UTF-8'))

    print(msg)