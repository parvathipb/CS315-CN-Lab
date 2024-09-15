import socket
import random

server_name = "Server"
# creating socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to get local machine name
LocalHostName = socket.gethostname()
# server port
port = 3600
server_socket.bind((LocalHostName, port))
server_socket.listen(1)

print(f"Server: Waiting...")

while(1):
    client_socket, SocketAddress = server_socket.accept()
    # receive client data, decode to utf-8
    client_data = client_socket.recv(1024).decode('utf-8')
    client_name, client_number = client_data.split()
    client_number = int(client_number)

    # checking if the number is out of range
    if client_number < 1 or client_number > 100:
        print("Received an integer value out of range. Terminating server.")
        client_socket.sendall('Out of range integer value sent. Terminating client.'.encode('utf-8'))
        break

    # to generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # send a message to the client, encode to utf-8
    client_socket.sendall(f"{server_name} {random_number}".encode('utf-8'))

    print(f"Client name: {client_name}, Server name: {server_name}")
    print(f"Client number: {client_number}, Server number: {random_number}")
    #print(f"Server number: {randNum}")
    print(f"Sum: {client_number + random_number}")

    # close the client socket
    client_socket.close()
# close the server socket
server_socket.close()