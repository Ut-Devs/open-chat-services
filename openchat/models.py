# from openchat import db
# from sqlalchemy.sql import func

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     message = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone = True), default = func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True, autoincrement = True)
#     password = db.Column(db.String(50))
#     first_name = db.Column(db.String(100))