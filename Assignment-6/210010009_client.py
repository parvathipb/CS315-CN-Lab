import socket
import random

def main(random_number):
    #random_number=111
    client_name = "Client"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # to get local machine name
    LocalHostName = socket.gethostname()
    # server port
    port = 3600
    client_socket.connect((LocalHostName, port))
    # sending message to the client, encode to utf-8
    client_socket.sendall(f"{client_name} {random_number}".encode('utf-8'))
    # receive data from the server
    received_data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {received_data}")
    # close the client socket
    client_socket.close()

def exit_program(random_number):
    while True:
        choice = input("Do you want to exit? (y/n): ").lower()
        if choice == 'y':
            # print("Exiting...")
            # print("Out of range number")
            random_number = random.randint(101, 200)
            main(random_number)
            break
        elif choice == 'n':
            main(random_number)
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    # to generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    main(random_number)
    exit_program(random_number)