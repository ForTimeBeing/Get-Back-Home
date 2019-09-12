#Run with python3
#Use ctrl + c to STOP the server
#else do: ps -fA | grep python
#find the server, kill it with
#sudo kill -9 PIDinTerminal

import http.server
import socketserver
import webbrowser

webbrowser.open('http://127.0.0.1:8080/')

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()