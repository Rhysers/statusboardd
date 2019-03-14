#!/usr/bin/env python3

import socket
from gpiozero import StatusZero

HOST = '127.0.0.5'
PORT = 65432

debugging = True
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
    board.one.pulse(2,2)
def internetBad():
    if debugging:
        print("Internet Red Light Blink")
    board.one.off()
    board.one.red.blink()
def alexaGood():
    if debugging:
        print("Alexa Green Light On")
    board.two.off()
    board.two.green.on()
def alexaWarning():
    if debugging:
        print("Alexa Green Light Pulse")
    board.two.off()
    board.two.green.pulse()
def alexaBad():
    if debugging:
        print("Alexa Red Light Pulse")
    board.two.off()
    board.two.red.pulse(2,2)
def googleGood():
    if debugging:
        print("Google Green Light On")
    board.three.off()
    board.three.green.on()
def googleBad():
    if debugging:
        print("Google Red Light On")
    board.three.off()
    board.three.green.on()

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
            eval(stringOut)