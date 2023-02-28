from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return '{ "message":"Open chat server", }'


@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)
