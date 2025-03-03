# -*- coding: utf-8 -*-
"""
Created on Mon Mar 3 7:10:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Multi Ping")
print(Fore.GREEN+font)

import subprocess

# Function to ping the IP address
def ping_ip(ip_address):
    """Ping the given IP address and return if it is reachable."""
    try:
        # Sending one ping request to the IP address
        response = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            return True  # IP is reachable
        else:
            return False  # IP is unreachable
    except Exception as e:
        print(f"Error while pinging {ip_address}: {e}")
        return False

def main():
    
    
    # Prompt the user to enter how many IP addresses they want to ping
    try:
        num_ips = int(input("How many IP addresses do you want to ping?"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if num_ips <= 0:
        print("Please enter a positive number of IP addresses.")
        return
    
    # Perform the ping operation for each IP address
    for i in range(num_ips):
        ip_address = input(f"Enter IP address {i + 1}: ").strip()
        
        # Ping the IP address and check if it's reachable
        print(f"Pinging {ip_address}...")
        if ping_ip(ip_address):
            print(f"{ip_address} is reachable.")
        else:
            print(f"{ip_address} is not reachable.")
    
    print("Ping process completed.")

if __name__ == "__main__":
    main()
