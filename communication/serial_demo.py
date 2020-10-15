"""
To list ports (Mac/Linux):

ls /dev/tty.*
"""

import time
import serial
import datetime as dt

# This has to be changed to your own device
device_name = '/dev/tty.usbmodem143301'

conn = serial.Serial(device_name, 9600)

while True:

    try:

        t_now = time.time()
        timestamp_now = dt.datetime.fromtimestamp(t_now).strftime('%Y-%m-%d %H:%M:%S.%f')

        line = conn.readline()
        
        print('[{}] {}'.format(timestamp_now, line))

    except KeyboardInterrupt:
        print('\nStopping the server due to keyborard interrupt')
        break
