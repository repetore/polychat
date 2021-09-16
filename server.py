import socket, time


host = socket.gethostbyname(socket.gethostname()) # 169.254.57.145
port = 9090
print(host)

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

running = True
print(" ::[POLYCHAT STARTED]:: ")

while running:
	# try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)


		print(f'{addr}: {data.decode("utf-8")}')

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	# except:
	# 	print("\n::[POLYCHAT STOPPED]::")
	# 	running = False
s.close()