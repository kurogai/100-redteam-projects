# Developed By: manthanghasadiya
# Contact the developer at: https://github.com/manthanghasadiya

import argparse
from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt, Dot11, RadioTap
from tabulate import tabulate
import os
import time

def list_interfaces():
    interfaces = [i[1] for i in socket.if_nameindex()]
    return interfaces

def select_interface(interfaces):
    for idx, iface in enumerate(interfaces, 1):
        print(f"{idx}. {iface}")
    selection = int(input("Select interface: "))
    return interfaces[selection - 1]

def is_in_monitor_mode(interface):
    result = os.popen(f"iwconfig {interface}").read()
    return "Mode:Monitor" in result

def put_in_monitor_mode(interface):
    if not is_in_monitor_mode(interface):
        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo iwconfig {interface} mode monitor")
        os.system(f"sudo ifconfig {interface} up")

def parse_arguments():
    interfaces = list_interfaces()
    selected_interface = select_interface(interfaces)

    parser = argparse.ArgumentParser(description="WiFi Monitor Tool")
    parser.add_argument("-i", "--interface", default=selected_interface, help="Interface to monitor")
    return parser.parse_args()

def format_packet_info(packet):
    if Dot11Beacon in packet:
        ssid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr3
        signal_strength = packet.dBm_AntSignal
        frequency = packet[RadioTap].ChannelFrequency
        data_rate = packet[RadioTap].Rate
        return [ssid, bssid, signal_strength, frequency, data_rate]

def monitor_wifi(interface):
    wifi_data = []
    unique_ssids = set()

    def packet_handler(packet):
        packet_info = format_packet_info(packet)
        if packet_info and packet_info[0] not in unique_ssids:
            wifi_data.append(packet_info)
            unique_ssids.add(packet_info[0])

    try:
        put_in_monitor_mode(interface)
        print(f"Putting {interface} into monitor mode... Done")
        print("Monitoring WiFi... Press Ctrl+C to stop.")
        sniff(iface=interface, prn=packet_handler, timeout=10)
        if wifi_data:
            headers = ["SSID", "BSSID", "Signal Strength (dBm)", "Frequency (MHz)", "Data Rate (Mbps)"]
            print(tabulate(wifi_data, headers=headers, tablefmt="grid"))
        else:
            print("No unique SSIDs found.")
    except KeyboardInterrupt:
        pass

def main():
    args = parse_arguments()
    monitor_wifi(args.interface)

if __name__ == "__main__":
    main()
