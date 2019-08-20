#!/usr/bin/python

import socket
from termcolor import colored

# afintet ipv4 sockstream tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.setdefaulttimeout(3.0) # doesn't seem to work

host = input("Enter the target IP: ")
# port = int(input("Enter the target Port #: "))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print (colored("Port %d is closed" % (port), 'red'))
    else:
        print (colored("Port %d is open" % (port), 'green'))

for port in range(1, 100):
    portscanner(port)
