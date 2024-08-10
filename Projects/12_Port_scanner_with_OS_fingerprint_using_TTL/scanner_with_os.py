# coding:utf-8

import sys
import threading
from queue import Queue
from scapy.all import *
import socket
import logging
from scapy.layers.inet import IP, ICMP
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress Scapy warning messages
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


# Define the port scanning function
def port_scan(ip, port, open_ports):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)  # Set connection timeout to 0.2 seconds
        sock.connect((ip, port))  # Attempt to connect to the specified IP and port
        open_ports.put(port)  # If connection is successful, add the port number to the queue
        sock.close()  # Close the connection
    except:
        pass  # Ignore exceptions if connection fails


# Analyze OS based on TTL
def analyze_os(ip, port):
    try:
        # Send ICMP request packet, try to get a response
        ans = sr1(IP(dst=ip) / ICMP(id=RandShort()), timeout=1, retry=2, verbose=0)

        if ans:  # If a response is received
            ttl = ans[IP].ttl  # Get the TTL value from the response packet

            # Guess the OS type based on TTL value
            if ttl <= 64:
                os_guess = "Linux or Unix"
            elif ttl == 108:
                os_guess = "Window2000"
            elif ttl == 107:
                os_guess = "win NT"
            elif ttl == 127:
                os_guess = "win9x"
            elif ttl == 252:
                os_guess = "Solaris"
            elif ttl == 128:
                os_guess = "Windows"
            else:
                os_guess = "Unix"

            # Print the port, TTL value, and the guessed OS type
            print(f"{ip}, port open: {port}, TTL: {ttl}, OS: {os_guess}")

    except Exception as e:
        pass  # Ignore exceptions


# Scan all ports of the target IP
def port_scan_all(ip):
    open_ports = Queue()  # Create a queue to store open ports

    # Use ThreadPoolExecutor to create a thread pool with 50 threads
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Submit all port scan tasks to the thread pool
        futures = [executor.submit(port_scan, ip, port, open_ports) for port in range(1, 65536)]

        # Wait for all threads to complete
        for future in as_completed(futures):
            pass

    open_port_list = []  # Convert the queue to a list
    while not open_ports.empty():
        open_port_list.append(open_ports.get())

    return open_port_list


# Main function to perform OS detection and port scanning
def main():
    if len(sys.argv) == 2:  # If a target IP address is provided
        ip_target = sys.argv[1]

        # Perform port scan and get the list of open ports
        open_ports = port_scan_all(ip_target)

        # Analyze TTL for each open port to guess the OS
        for port in open_ports:
            analyze_os(ip_target, port)

    else:  # If no target IP address is provided
        print("Correct usage: script, IP address target")
        sys.exit(0)


# Execute the main function
if __name__ == "__main__":
    main()
