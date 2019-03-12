
import socket

chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created!")

PORT = 8080
IP = "10.3.50.228"

chat_socket.connect((IP, PORT))

while True:
    chat_socket.send(str.encode(input("You: ")))
    msg = chat_socket.recv(2048).decode("utf-8")
    print("Server:", msg)
