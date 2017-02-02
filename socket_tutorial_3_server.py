#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 12:48 PM

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(socket_family, socket_type, protocol=0)

'''
socket_family: Defines the family of protocols used as the transport mechanism. It can have either of the two values.
Either AF_UNIX, or AF_INET (IP version 4 or IPv4).
socket_type: Defines the types of communication between the two end-points. It can have following values.
    SOCK_STREAM (for connection-oriented protocols e.g. TCP), or
    SOCK_DGRAM (for connectionless protocols e.g. UDP).
protocol: We typically leave this field or set this field to zero.
'''
#bind() is used to associate the socket with the server address
# Bind the socket to the port
hostname, aliases, address = socket.gethostbyaddr(socket.gethostname())
server_address = (address[0], 10000) #(host, port)

print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection
# is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv()
#  and transmitted with sendall().

try:
    print >> sys.stderr, 'connection from', client_address

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(16)
        print >> sys.stderr, 'received "%s"' % data
        if data:
            print >> sys.stderr, 'sending data back to the client'
            connection.sendall(data)
        else:
            print >> sys.stderr, 'no more data from', client_address
            break

finally:
    # Clean up the connection
    connection.close()