# Based on
# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect('tcp://localhost:5556')

socket.setsockopt(zmq.SUBSCRIBE, b'10001')
socket.setsockopt(zmq.SUBSCRIBE, b'10002')

for update_nbr in range(5):
    
    message = socket.recv()
    topic, messagedata = message.split()
    print(topic, messagedata)
