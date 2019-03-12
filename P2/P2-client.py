import socket

p2socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080
IP = "192.168.1.49"
p2socket.connect((IP, PORT))

# Now, we design the simple response loop
while True:
    p2socket.send(str.encode(input("Sequence: ")))
    result = p2socket.recv(2048).decode("utf-8")
    print("Server:", result)

