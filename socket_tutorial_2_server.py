#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on November 06, 2016 by 9:47 PM

import socket
import sys
import time

# sock_obj = socket.socket(socket_family, socket_type, protocol=0)
# Instantiate an AF_INET, STREAM socket (TCP)

# try:
#     # create an AF_INET, STREAM socket (TCP)
#     sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# except socket.error as err_msg:
#     print ('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ' , Error message : ' + err_msg[1])
#     sys.exit();
#
# print ('Socket Initialized')



def Main():
    '''
    Whenever a client gets connected, the server accepts that connection.
The client will then start passing messages to the server.
And the server will process those messages and send the response back to the client.
In the below code, we are also asking the user to input his response that he wants to pass to the client.
    :return:
    '''
    host = "127.0.0.1"
    port = 5002

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print ("from connected  user: " + str(data))

        data = str(data).upper()
        print ("Received from User: " + str(data))

        data = str(raw_input(" ? "))
        conn.sendall(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()

