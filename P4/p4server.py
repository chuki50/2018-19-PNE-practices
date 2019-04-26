import socket
import termcolor

IP = "172.72.15.169"
PORT = 8081

MAX_OPEN_REQUESTS = 5


def process_client(cs):

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # Now we want the first line of the message, so we can get the path.
    msg_lines = msg.splitlines()
    first_line = msg_lines[0]
    termcolor.cprint(first_line, 'cyan')

    # In order to know what the user wants to do, we define the 4 options.
    if first_line.startswith("GET /") or first_line.startswith("GET  "):
        file_name = "index.html"
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {} \r\n".format(len(str.encode(content)))
        response_msg = status_line + header + "\r\n" + content

    elif first_line.startswith("GET /blue.html"):
        file_name = "blue.html"
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {} \r\n".format(len(str.encode(content)))
        response_msg = status_line + header + "\r\n" + content

    elif first_line.startswith("GET /pink.html"):
        file_name = "pink.html"
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {} \r\n".format(len(str.encode(content)))
        response_msg = status_line + header + "\r\n" + content

    else:
        file_name = "error.html"
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        status_line = "HTTP/1.1 200 ok\r\n"

        header = "Content-Type: text/html\r\n"
        header += "Content-Length: {} \r\n".format(len(str.encode(content)))
        response_msg = status_line + header + "\r\n" + content

    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
