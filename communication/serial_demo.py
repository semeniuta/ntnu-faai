"""
To list ports:

ls /dev/tty.*
"""

from time import sleep
import serial

conn = serial.Serial('/dev/tty.usbmodem1432301', 9600)

while True:

    try:

        line = conn.readline()
        print(line)

    except KeyboardInterrupt:
        print('\nStopping the server due to keyborard interrupt')
        break
