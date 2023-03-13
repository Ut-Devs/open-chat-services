from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app, cors_allowed_origins="*")
bcrypt = Bcrypt(app)
db.init_app(app)
ma.init_app(app)

from .routes import routes
from .models import User

with app.app_context():
    db.create_all()




