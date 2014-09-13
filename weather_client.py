import zmq
import sys


class WeatherClient:
	def __init__(self, port, zip):
		context = zmq.Context()
		self.socket  = context.socket(zmq.SUB)
		self.socket.connect('tcp://localhost:' + str(port))
		self.socket.setsockopt_string(zmq.SUBSCRIBE, str(zip))

	def receive(self):
		return (self.socket.recv_string())

def main():
	port = sys.argv[1]
	zip  = sys.argv[2]
	client = WeatherClient(port, zip)
	print(client.receive())
	return 0

if __name__ == '__main__':
	sys.exit(main())

		
