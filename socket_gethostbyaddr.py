#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 08, 2016 by 12:28 PM
'''
When the address of a server is available, use gethostbyaddr() to do a “reverse” lookup for the name.
'''
import socket


# hostname, aliases, addresses = socket.gethostbyaddr('127.0.1.1') #you can use ip-address or hostname as argument see line 17
#
# print 'Hostname :', hostname
# print 'Aliases  :', aliases
# print 'Addresses:', addresses

# print socket.gethostname()
a,b,c =  socket.gethostbyaddr(socket.gethostname())
print type(c[0])