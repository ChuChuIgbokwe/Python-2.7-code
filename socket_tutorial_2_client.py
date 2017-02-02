#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 06, 2016 by 10:26 PM

import socket


def Main():
    '''
    On the client side, we create a socket and connect to the server using the supplied host and port values.

Client code has a while loop for exchanging messages. The loop keeps printing all the data obtained from the server.
After this, there is a call to the input function asking for the client response. The response is then forwarded to the
server.
The user may also enter ‘q’ to stop the communication at any point in time.

    :return:
    '''
    host = '127.0.0.1'
    port = 5002

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(" ? ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print ('Received from server: ' + data)

        message = str(raw_input(" ? "))

    mySocket.close()


if __name__ == '__main__':
    Main()