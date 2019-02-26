import socket

PORT = 8080
IP = "10.3.50.147"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from client: {}".format(msg))

    # Sending the message back to the client, since we are an echo server


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready at: {}".format(serversocket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    print("Attending connections from client: {}".format(address))

    clientsocket.close()
