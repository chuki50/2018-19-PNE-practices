import socket
from P1.Seq import Seq

# We use our current IP and we choose a PORT for our server.
IP = '10.3.53.128'
PORT = 8080
MAX_OPEN_REQUESTS = 5
number_con = 0

# We create the socket
p2socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


p2socket.bind((IP, PORT))
p2socket.listen(MAX_OPEN_REQUESTS)
try:
    # We create a loop that answers to the client, taking the class from P1, and returning the
    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (client_socket, address) = p2socket.accept()
        number_con += 1

        print("Connection: {}. From the IP: {}".format(number_con, address))

        seq_received = Seq(client_socket.recv(2048).decode("utf-8"))
        print("Sequence received: {}".format(seq_received))

        seq_reversed = str(seq_received.reverse())
        seq_complemented = str(seq_received.complementary())

        result = str.encode("Complementary: {}. Reversed: {}".format(seq_complemented, seq_reversed))
        client_socket.send(result)
        client_socket.close()


except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    p2socket.close()
