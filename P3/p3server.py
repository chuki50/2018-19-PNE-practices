import socket

# IP and PORT of our server
IP = "10.3.53.128"
PORT = 8081
MAX_OPEN_REQUEST = 5


def process_client(clientsocket):
    # Reading the message from the client.
    print("Hello")
    msg = clientsocket.recv(2048).decode("utf-8")
    msg = msg.split('\n')
    first_line = msg[0]

    null_first = False
    invalid_first = False

    if first_line == "":
        null_first = True
        msg_alive = "ALIVE"
        clientsocket.send(str.encode(msg_alive))
    else:
        for base in range(len(first_line)):
            if first_line[base] not in ["A", "T", "G", "C"]:
                invalid_first = True
                break
            else: continue

    # We define each of the operations that the client can ask.
    if invalid_first:
        msg_invalid = "One of the bases of your sequence is invalid"
        clientsocket.send(str.encode(msg_invalid))

    elif not null_first and not invalid_first:
        operation_lines = msg[1:]
        answer_list = []

        for x in range(len(operation_lines)):
            if operation_lines[x] == "len":
                length = len(first_line)
                answer_list.append(length)

            elif operation_lines[x] == "complement":
                notcompl = str(first_line)
                complementary_seq = ''
                for i in range(len(notcompl)):
                    if notcompl[i] == 'A':
                        complementary_seq = complementary_seq + 'T'
                    elif notcompl[i] == 'T':
                        complementary_seq = complementary_seq + 'A'
                    elif notcompl[i] == 'C':
                        complementary_seq = complementary_seq + 'G'
                    elif notcompl[i] == 'G':
                        complementary_seq = complementary_seq + 'C'
                answer_list.append(complementary_seq)

            elif operation_lines[x] == "reverse":
                reverse_seq = first_line[::-1]
                return reverse_seq

            elif operation_lines[x] == "countA":
                counterA = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'A':
                        counterA += 1
                answer_list.append(counterA)

            elif operation_lines[x] == "countT":
                counterT = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'T':
                        counterT += 1
                answer_list.append(counterT)

            elif operation_lines[x] == "countG":
                counterG = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'G':
                        counterG += 1
                answer_list.append(counterG)

            elif operation_lines[x] == "countC":
                counterC = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'C':
                        counterC += 1
                answer_list.append(counterC)

            elif operation_lines[x] == "percA":
                counterA = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'A':
                        counterA += 1
                percentageA = 100 * (counterA / len(first_line))
                answer_list.append(percentageA)

            elif operation_lines[x] == "percT":
                counterT = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'T':
                        counterT += 1
                percentageT = 100 * (counterT / len(first_line))
                answer_list.append(percentageT)

            elif operation_lines[x] == "percG":
                counterG = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'G':
                        counterG += 1
                percentageG = 100 * (counterG / len(first_line))
                answer_list.append(percentageG)

            elif operation_lines[x] == "percC":
                counterC = 0
                for i in range(len(first_line)):
                    if first_line[i] == 'C':
                        counterC += 1
                percentageC = 100 * (counterC / len(first_line))
                answer_list.append(percentageC)

            else:
                print("One option was found invalid")

        print(answer_list)
        answer_list = str(answer_list)
        msg_send = answer_list.replace(",", "\n").strip("[").strip("]")
        clientsocket.send(str.encode(msg_send))

    # Close the socket
    clientsocket.close()


# Create a socket for connecting to the clients
p3socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

p3socket.bind((IP, PORT))
p3socket.listen(MAX_OPEN_REQUEST)

print("Socket ready at: {}".format(p3socket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (c3socket, address) = p3socket.accept()

    print("Attending connections from client: {}".format(address))
    process_client(c3socket)
