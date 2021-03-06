#!/usr/bin/env python3

import socket
from gpiozero import StatusZero

HOST = '127.0.0.5'
PORT = 65432

debugging = False
board = StatusZero( pwm=True )


def internetGood():
    if debugging:
        print("Internet Green Light On")
    board.one.off()
    board.one.green.on()
def internetOK():
    if debugging:
        print("Internet Green Light Pulse")
    board.one.off()
    board.one.green.pulse(2,2)
def internetBad():
    if debugging:
        print("Internet Red Light Blink")
    board.one.off()
    board.one.red.blink()
def noUpdates():
    if debugging:
        print("Updates Green Light On")
    board.two.off()
    board.two.green.on()
def secUpdates():
    if debugging:
        print("Updates red Light Pulse")
    board.two.off()
    board.two.red.pulse()
def updates():
    if debugging:
        print("Upddates Red Light On")
    board.two.off()
    board.two.red.on()
def needReboot():
    if debugging:
        print("Updates Blink")
    board.two.off()
    board.two.blink()
def alexaGood():
    if debugging:
        print("Alexa Green Light On")
    board.three.off()
    board.three.green.on()
def alexaWarning():
    if debugging:
        print("Alexa Green Light Pulse")
    board.three.off()
    board.three.green.pulse()
def alexaBad():
    if debugging:
        print("Alexa Red Light Pulse")
    board.three.off()
    board.three.red.pulse(2,2)
def stop():
    quit()

valid = 'internetGood()', 'internetOK()', 'internetBad()', 'alexaGood()', 'alexaWarning()', 'alexaBad()', 'stop()', 'noUpdates()', 'secUpdates()', 'updates()', 'needReboot()'

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()
        with conn:
            dataout = b''
            while True:
                data = conn.recv(1024)
                dataout += data
                if not data:
                    break
            stringOut=dataout.decode()
            if stringOut in valid:
                eval(stringOut)
            else:
                if debugging:
                    print('invalid input detected '+stringOut)
                continue
