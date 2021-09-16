import socket, threading, time


class Client:
	def __init__(self):
		self.host = socket.gethostbyname(socket.gethostname())
		self.port = 0
		# self.server = "169.254.57.145" 
		# self.server = "172.16.93.73"
		self.server = "172.16.93.243"

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind((self.host, self.port))
		self.socket.setblocking(0)
		self.running = True
		self.read_thread = threading.Thread(target = self.receiving)


	def receiving(self):
		while self.running:
			try:
				data, address = self.socket.recvfrom(1024)
				print(f'{address}: {data.decode("utf-8")}')
			except:
				pass




	def loop(self):
		while self.running:
			try:
				message = input("")
				if message != "":
					self.socket.sendto(message.encode('utf-8'), (self.server, 9090))

			except:
				self.running = False


	def run(self):
		self.read_thread.start()
		self.loop()
		self.read_thread.join()
		self.socket.close()




client = Client()
client.run()



