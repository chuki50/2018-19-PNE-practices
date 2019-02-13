import socket

PORT = 8080
IP = "10.3.53.54"
max_requests = 5

# Counting the number of connections
connections = 0

# create an INET, STREAMing socket

chatsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    chatsocket.bind((IP, PORT))
    chatsocket.listen(max_requests)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = chatsocket.accept()

        connections += 1

        print("Connection: {}. From the IP: {}".format(connections, address))

        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        message = str(input("Type your message here: "))
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    chatsocket.close()