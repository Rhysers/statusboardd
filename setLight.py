#/usr/bin/env python3
import sys, socket

HOST = '127.0.0.5'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

myInput = str(sys.argv[1])

if myInput == "1":
    myOutput = b'internetGood()'
elif myInput == "2":
    myOutput = b'internetOK()'
elif myInput == "3":
    myOutput = b'internetBad()'
elif myInput == '4':
    myOutput = b'noUpdates()'
elif myInput == '5':
    myOutput = b'secUpdates()'
elif myInput == '6':
    myOutput = b'updates()'
elif myInput == '7':
    myOutput = b'needReboot()'


#print(myOutput)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socks:
    socks.connect((HOST, PORT))
    socks.sendall(myOutput)