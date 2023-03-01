from flask import Flask
import os
import json
import uuid
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def connect():
    emit('session', {'id': str(uuid.uuid4())})
@socketio.on('sendMessage')
def send_message(data):
    print(data)
    emit('messageReceived', json.loads(data), broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
