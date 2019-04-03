import socket

# IP and PORT of our server
IP = "192.168.2.216"
PORT = 8080

MAX_OPEN_REQUEST = 5

def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")
    msg = msg.split('/')
    first_line = msg[0]
    operation_lines = msg[1:]

    answer_list = []

    null_first = False
    invalid_first = False

    if first_line == "":
        null_first = True

    while not null_first:
        for x in range(len(first_line)):
            if first_line[x] not in ["A","T","G","C"]:
                invalid_first = True
                break
            else:
                continue


    while not invalid_first:
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

    answer_list = str(answer_list)
    msg_send = answer_list.replace(",", "\n")

    cs.send(str.encode(msg_send))
    # Close the socket
    cs.close()


# Create a socket for connecting to the clients
p3socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

p3socket.bind((IP, PORT))

p3socket.listen(MAX_OPEN_REQUEST)

print("Socket ready at: {}".format(p3socket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = p3socket.accept()

    print("Attending connections from client: {}".format(address))
    process_client(clientsocket)
    clientsocket.close()
