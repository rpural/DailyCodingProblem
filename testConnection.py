#! /usr/bin/env python2.7

#!/usr/bin/env python

import socket
import sys

sock = ( sys.argv[1], int(sys.argv[2]) )

BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(sock)
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
