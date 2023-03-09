from openchat import db
import json
import uuid
from flask_cors import CORS
from flask import request, jsonify
from flask_socketio import SocketIO, emit
from ..models.User import User, user_schema, users_schema
from openchat import app

CORS(app, resources={r"/api/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/user', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        first_name = data['first_name']
        password = data['password']
        user = User(first_name, password)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'Success in insertion', 'data': result}), 201
    else:
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify({'message': 'Success in fetching', 'data': result}), 200

@socketio.on('connect')
def connect():
    emit('session', {'id': str(uuid.uuid4())})

@socketio.on('sendMessage')
def send_message(data):
    emit('messageReceived', json.loads(data), broadcast=True)