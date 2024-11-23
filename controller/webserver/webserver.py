from flask import Flask, render_template, Blueprint
from flask_sockets import Sockets
import os
import re

app = Flask(__name__)
sockets = Sockets(app)

@app.route("/")
def index():
    return render_template("index.html")

@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print(message)
        ws.send(message)

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()