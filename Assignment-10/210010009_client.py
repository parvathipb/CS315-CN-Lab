from socket import *
import time

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ("127.0.0.1", 12000)
clientSocket.settimeout(1)
 
# Send to server using created UDP socket
for i in range(10):
	message = f'Ping {i + 1} {time.ctime()}'
	currentTime = time.time()
	# print(current_Time)
	clientSocket.sendto(message.encode(), serverAddress)

	try:
		message, address = clientSocket.recvfrom(1024)
	except timeout:
		print(f'# {i + 1} Request Timed Out')
		continue

	endTime = time.time()
	# Calculating RTT
	RTT = endTime-currentTime
	print(f'# {i + 1} {message.decode()}', end="  ")
	print(f'RTT: {RTT*1000} milli seconds')
	