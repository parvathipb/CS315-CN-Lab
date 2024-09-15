# In browser: http://<ip_address>:3600/HelloWorld.html
import socket

port = 3600
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)
print ('The web server is up on port: ', port)

while True:
	print ('Ready...')
	# Set up a new connection from the client
	connection, address = server_socket.accept()

	try:
		message = connection.recv(1024)
		# print(f"{message}")
		filename = message.split()[1]
		# print(f"{filename}")
		# print(f"{filename[1:]}")
		inputFile = open(filename[1:])

		output_data =inputFile.read()
		# print (output_data)
		connection.send('\nHTTP/1.1 200 OK\n\n\n'.encode())

		# Send the content of the requested file to the connection socket
		for i in range(0, len(output_data)):
			# send one encoded byte at a time
			connection.send(output_data[i].encode())

		connection.send("\r\n".encode())
		# Close the client connection socket
		connection.close()

	# when file not found in server
	except IOError:
		output_data = '<html><h1>404 Not Found!</h1><html>'
		connection.send("\nHTTP/1.1 404 Not Found\n\n\n".encode())

		for i in range(0, len(output_data)):
			# send one encoded byte at a time
			connection.send(output_data[i].encode())
		# Close the client connection socket
		connection.close()
	choice = input("Do you want to exit? (y/n): ").lower()
	if choice == 'y':
		break
	elif choice == 'n':
		continue
	else:
		print("Invalid choice. Please enter 'y' or 'n'.")
# Close the server socket
server_socket.close()