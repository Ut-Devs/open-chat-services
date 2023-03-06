from openchat import db, ma
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(100))

    def __init__ (self, first_name, password):
        self.first_name = first_name
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


