#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 07, 2016 by 4:59 PM

import socket

print socket.gethostname()

for host in [ 'homer', 'www', 'www.python.org', 'nosuchname' ]:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)