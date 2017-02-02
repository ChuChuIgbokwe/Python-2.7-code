#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 07, 2016 by 5:05 PM

import socket
#For access to more naming information about a server, use gethostbyname_ex(). It returns the canonical hostname of the
# server, any aliases, and all of the available IP addresses that can be used to reach it.

for host in [ 'homer', 'www', 'www.python.org', 'nosuchname' ]:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print '    Hostname:', hostname
        print '    Aliases :', aliases
        print ' Addresses  :', addresses
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host,msg)
    print
