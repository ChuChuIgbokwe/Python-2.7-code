#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 05, 2016 by 7:36 PM

import socket

s = socket.socket()
host = '127.0.0.1'
port = 12345
#Bind
s.bind((host,port))
#listen
s.listen(5)
#accept
while True:
    c,addr = s.accept()
    print 'Got connection from ', addr
    c.send('Thank You for connecting')
    c.close()