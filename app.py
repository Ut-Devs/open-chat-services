from flask import Flask
import os
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/', methods=['GET'])
def index():
    return '{ "message":"Open chat server", }'


@sock.route('/echo', methods=['GET'])
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3333))
    app.run(debug=True, port=port)
