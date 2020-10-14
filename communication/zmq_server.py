# Example based on 
# https://zeromq.org/languages/python/

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:

    try:
        
        message = socket.recv()
        print('Received request: %s', message)

        number = float(message)
        response = b'ok' if number < 70 else b'high'

        time.sleep(1)

        socket.send(response)

    except KeyboardInterrupt:
        print('\nStopping the server due to keyborard interrupt')
        break
