import zmq

import sys

context = zmq.Context()

socket = context.socket(zmq.SUB)

socket.connect('tcp://localhost:5556')

socket.setsockopt_string(zmq.SUBSCRIBE, '10001')

str = socket.recv_string()

print(str)

