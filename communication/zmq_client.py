# Example based on
# https://zeromq.org/languages/python/

import zmq
import random

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for i in range(10):

    # random dunber between 0 and 100
    number = random.random() * 100
    
    message = '{:.3f}'.format(number).encode()

    print('Sending request:', message)
    
    socket.send(message)

    #  Get the reply.
    reply = socket.recv()
    print('Received reply:', reply)
    print()
