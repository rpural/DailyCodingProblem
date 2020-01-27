#! /usr/bin/env python2.7

#!/usr/bin/env python

import socket
import sys

if len(sys.argv) != 3:
    print "Usage:"
    print "  testConnection.py system-name portno"
    print "     - system-name is the name or IP address of the system you"
    print "       want to connect to"
    print "     - portno is the port number to be tested"
    print "    example: ./testConnection.py rofrpn801a 8080"
    exit(0)

try:
    sock = ( sys.argv[1], int(sys.argv[2]) )
except ValueError:
    print "Couldn't build an address from what you've given. Is your port number correct?"
    exit(1)

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(sock)
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
