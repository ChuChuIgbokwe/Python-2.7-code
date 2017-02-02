#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 1:06 PM

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
hostname, aliases, address = socket.gethostbyaddr(socket.gethostname())
server_address = (address[0], 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#After the connection is established, data can be sent through the socket with sendall()
# and received with recv(), just as in the server.

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >> sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()

