import os

DB_NAME = "database.db"
DEBUG = True
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')