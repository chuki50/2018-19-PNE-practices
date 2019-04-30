# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
import http.server
import socketserver
import termcolor
socketserver.TCPServer.allow_reuse_address = True
# Define the Server's port
PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'cyan')
        print("  Command: " + self.command)
        print("  Path: " + self.path)
        path = self.path

        if path == '' or path == '/':
            f = open('p6page.html', 'r')
            contents = f.read()
            f.close()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif path.startswith('/?'):
            cont = """<!DOCTYPE html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <title>Responses</title>
                          </head>
                            <h1>Responses from the sequence analyzed:</h1>
                            """
            operation_html = ""
            len_html = ""

            path_div = path.replace('/?', '')
            data = str(path_div).split('&')

            # First, we are going to work on the DNA sequence. We are going to obtain it from the first unit in data.
            seq_r = data[0].split('=')
            seq = str(seq_r[1])

            invalid = False

            # We don't want invalid bases, so we are going to run our sequence through a loop to detect non-valid bases.
            for base in range(len(seq)):
                if seq.upper()[base] not in ["A", "T", "G", "C"]:
                    invalid = True
                    break
                else:
                    continue

            len_opt = False
            if len(data) == 4:
                len_opt = True
                operation_r = data[2].split('=')
                operation = str(operation_r[1])
                base_r = data[3].split('=')
                base = str(base_r[1])

            else:
                operation_r = data[1].split('=')
                operation = str(operation_r[1])
                base_r = data[2].split('=')
                base = str(base_r[1])

            while not invalid:
                if len_opt:
                    seq_len = len(seq)
                    len_html = "<p>The length of the sequence is: {}</p>".format(seq_len)

                if operation == 'perc':
                    perc = float()
                    if base == 'A':
                        counterA = 0
                        for i in range(len(seq)):
                            if seq[i] == 'A':
                                counterA += 1
                        perc = 100 * (counterA / len(seq))
                    elif base == 'G':
                        counterG = 0
                        for i in range(len(seq)):
                            if seq[i] == 'G':
                                counterG += 1
                        perc = 100 * (counterG / len(seq))
                    elif base == 'C':
                        counterC = 0
                        for i in range(len(seq)):
                            if seq[i] == 'C':
                                counterC += 1
                        perc = 100 * (counterC / len(seq))
                    elif base == 'T':
                        counterT = 0
                        for i in range(len(seq)):
                            if seq[i] == 'T':
                                counterT += 1
                        perc = 100 * (counterT / len(seq))

                    operation_html = "<p>The percentage of the base {} is: {}% </p>".format(base, perc)

                elif operation == 'count':
                    count = int()
                    if base == 'A':
                        counterA = 0
                        for i in range(len(seq)):
                            if seq[i] == 'A':
                                counterA += 1
                        count = counterA
                    elif base == 'G':
                        counterG = 0
                        for i in range(len(seq)):
                            if seq[i] == 'G':
                                counterG += 1
                        count = counterG

                    elif base == 'C':
                        counterC = 0
                        for i in range(len(seq)):
                            if seq[i] == 'C':
                                counterC += 1
                        count = counterC

                    elif base == 'T':
                        counterT = 0
                        for i in range(len(seq)):
                            if seq[i] == 'T':
                                counterT += 1
                        count = counterT

                    operation_html = "<p>The number of {} bases is: {} </p>".format(base, count)

                cont1 = cont + "\r\n" + len_html + "\r\n" + operation_html + "\r\n"
                cont2 = """</body>
                        </html>"""
                response = cont1 + cont2

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(response)))
                self.end_headers()
                self.wfile.write(str.encode(response))

            if invalid:
                f = open("error.html",'r')
                response = f.read()
                f.close()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(response)))
                self.end_headers()
                self.wfile.write(str.encode(response))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT: ", PORT)

    # -- Main loop: Attend the client.
    # -- Whenever there is a new client, the handler is called.
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
