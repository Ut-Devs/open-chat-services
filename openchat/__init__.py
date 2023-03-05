from flask import Flask, request, jsonify
import json
import uuid
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    ma.init_app(app)


    with app.app_context():
        db.create_all()
    
    from .models.User import User, user_schema, users_schema


    CORS(app,resources={r"/api/*":{"origins":"*"}})
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

    return app
