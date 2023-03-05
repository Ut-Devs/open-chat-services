from flask import Flask
import os
import json
import uuid
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    cors = CORS(app,resources={r"/api/*":{"origins":"*"}})
    socketio = SocketIO(app, cors_allowed_origins="*")

    @app.route('/')
    def index():
        return 'Hello World'

    @socketio.on('connect')
    def connect():
        emit('session', {'id': str(uuid.uuid4())})

    @socketio.on('sendMessage')
    def send_message(data):
        print(data)
        emit('messageReceived', json.loads(data), broadcast=True)

    return app
