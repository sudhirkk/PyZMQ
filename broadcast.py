import zmq
import time
import sys
from random import randrange


class Weather:
	def __init__(self):
		self.zipcode     = 0
		self.temperature = 0
		self.humidity    = 0

	def init(self):
		self.zipcode     = randrange(1, 100000)
		self.temperature = randrange(-80, 135)
		self.humidity    = randrange(10, 60)
	

class BroadcastServer:
	def __init__(self, port):
		self.context = zmq.Context()
		self.port    = port
		self.socket  = self.context.socket(zmq.PUB)
		self.weather = Weather()
	
	def publish(self):
		self.weather.init()
		self.socket.send_string(('%i %i %i') % (self.weather.zipcode, \
			self.weather.temperature, self.weather.humidity))
		
	def start(self):
		self.socket.bind('tcp://*:' + str(self.port))
		while True:
			time.sleep(0.1)
			self.publish()
					


def main():
	port = sys.argv[1]
	server = BroadcastServer(port)
	server.start()
	
if __name__ == '__main__':
	sys.exit(main())


