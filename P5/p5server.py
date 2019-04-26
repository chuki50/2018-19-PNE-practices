import http.server
import socketserver
import termcolor

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'cyan')
        print("  Command: " + self.command)
        print("  Path: " + self.path)

        path = self.path
        req = self.requestline

        # In order to know what the user wants to do, we define the 4 options.
        if path == "/" or path == "/index.html":
            file_name = "index.html"
            f = open(file_name, 'r')
            content = f.read()
            f.close()

        elif req.startswith("GET /blue.html"):
            file_name = "blue.html"
            f = open(file_name, 'r')
            content = f.read()
            f.close()

        elif req.startswith("GET /pink.html"):
            file_name = "pink.html"
            f = open(file_name, 'r')
            content = f.read()
            f.close()

        else:
            file_name = "error.html"
            f = open(file_name, 'r')
            content = f.read()
            f.close()

        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(content))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
