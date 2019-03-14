#!/usr/bin/env python3

import socket

HOST = '127.0.0.5'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

myFunction=input('Command:')
outString = myFunction.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(outString)
#    data = s.recv(1024)

print('Sent') #, repr(data))
