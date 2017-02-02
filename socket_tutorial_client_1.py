#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 05, 2016 by 8:07 PM

import socket
s = socket.socket()
host = '127.0.0.1'
port = 12345
s.connect((host, port))
print s.recv((1024))
s.close()