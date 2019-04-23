# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        path = self.path
        message_recieved = str(path)[10:]
        termcolor.cprint(self.requestline, 'green')

        # Open the form.html file
        f = open("ex1-echorequest.html", 'r')
        contents = f.read()
        print(contents)
        # Generating the response message
        self.send_response(200)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return message_recieved


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
