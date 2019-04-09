import socket

# SERVER IP, PORT
IP = "10.3.53.128"
PORT = 8081

# Before connecting to the server, ask the user for the string
msg = """AAAPACCGGGT\nlen\ncountA"""

# Now we can create the socket and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode("utf-8")
print(response)
s.close()
