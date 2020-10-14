# Based on
# https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:5556')

while True:

    try:
    
        topic = random.randrange(9999, 10005)
        messagedata = random.randrange(1, 215) - 80

        update_message = '{} {}'.format(topic, messagedata)
        
        print(update_message)
        
        socket.send_string(update_message)

        time.sleep(1)

    except KeyboardInterrupt:
        print('\nStopping the server due to keyborard interrupt')
        break
