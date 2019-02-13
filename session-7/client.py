# Programming our first client

import socket

# Create a socket in order to communicate with the server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created!")

PORT = 8081
IP = '212.128.253.84'

s.connect((IP, PORT))

s.send(str.encode("crying"))

msg = s.recv(2048).decode("utf-8")

print("Message receieved:")
print(msg)

s.close()

print("The End")
