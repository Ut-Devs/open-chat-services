from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
ma.init_app(app)

from .routes import routes
