import socket

p2socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 8080
IP = "10.3.53.128"


# Now, we design the simple response loop
p2socket.connect((IP, PORT))
p2socket.send(str.encode(input("Sequence: ")))
result = p2socket.recv(2048).decode("utf-8")
print("Server:", result)
p2socket.close()

