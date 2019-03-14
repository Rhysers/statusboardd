#/usr/bin/env python3
import sys, socket

HOST = '127.0.0.5'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

myInput = str(sys.argv[1])

if myInput == "1":
    myOutput = b'InternetGood()'
elif myInput == "2":
    myOutput = b'InternetOK()'
elif myInput == "3":
    myOutput = b'InternetBad()'

#print(myOutput)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socks:
    socks.connect((HOST, PORT))
    socks.sendall(myOutput)