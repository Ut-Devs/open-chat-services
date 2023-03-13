from openchat import app, db, ma, bcrypt
import datetime as dt
import jwt
    
class User(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)

    def __init__ (self, email, password, first_name, registered_on):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.first_name = first_name
        self.registered_on = registered_on

    def encode_auth_token(self, user_id):

        # So, given a user id, this method creates and returns a token from the payload and the secret key set in the config.py file
        # The payload is where we add metadata about the token and information about the user.

        try:
            payload = {
                'exp': dt.datetime.utcnow() + dt.timedelta(minutes=10),
                'iat': dt.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'registered_on', 'first_name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


