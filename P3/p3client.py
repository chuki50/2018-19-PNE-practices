import socket

# SERVER IP, PORT
IP = "192.168.2.216"
PORT = 8080



while True:

    # Before connecting to the server, ask the user for the string
    msg = input("Introduce your sequence and the operations separated by /n:")

    # Now we can create the socket and connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode("utf-8")

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
