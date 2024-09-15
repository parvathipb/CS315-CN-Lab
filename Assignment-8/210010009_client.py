#add in prompt
from socket import *
import ssl
from ssl import SSLContext
import base64
from base64 import b64encode

userEmail = "smtplab23@gmail.com"
userPassword = "lmvgusmmhxkmzoti"
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")
# Check if the subject is empty or contains only whitespace
if not userSubject.strip():
    msg = '{}.\r\n I love computer networks!'.format(userBody)
else:
    # Create the email message with subject and body
    msg = f"Subject: {userSubject}\r\n\r\n{userBody}.\r\n I love computer networks!"


# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailServer = "smtp.gmail.com"
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, 587))  # using port 587 for secure SMTP connection
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
#account authentication
clientSocket.send("STARTTLS\r\n".encode())
clientSocket.recv(1024).decode()
sslClientSocket = ssl.wrap_socket(clientSocket)
sslClientSocket.send("AUTH LOGIN\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userEmail.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
sslClientSocket.send(b64encode(userPassword.encode()) + "\r\n".encode())
print(sslClientSocket.recv(1024))
# Send MAIL FROM command and print server response.
#Fill in start
sslClientSocket.send("MAIL FROM:<smtplab23@gmail.com>\r\n".encode())
recv2 = sslClientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('555 250 reply not received from server.')
#Fill in end
# Send RCPT TO command and print server response.
#Fill in start
sslClientSocket.send(f"RCPT TO:<{userDestinationEmail}>\r\n".encode())
recv3 = sslClientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('556 250 reply not received from server.')
#Fill in end
# Send DATA command and print server response.
#Fill in start
sslClientSocket.send("DATA\r\n".encode())
recv4 = sslClientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
#Fill in end
# Send message data.
#Fill in start
sslClientSocket.send(msg.encode())
#Fill in end
# Message ends with a single period.
#Fill in start
sslClientSocket.send("\r\n.\r\n".encode())
recv5 = sslClientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')
#Fill in end
# Send QUIT command and get server response.
#Fill in start
sslClientSocket.send("QUIT\r\n".encode())
recv6 = sslClientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
#Fill in end

# close the socket
sslClientSocket.close()