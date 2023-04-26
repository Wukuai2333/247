from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class NoteName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # the number indicates the maximum length of characters that can be stored in the colums
    data = db.Column(db.String(1000000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_name = db.relationship('NoteName', backref='note', uselist=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


# class Event(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     description = db.Column(db.String(500))
#     date = db.Column(db.Date)
#     location = db.Column(db.String(100))
#     event_signups = db.relationship('EventSignup', backref='event', lazy=True)

#     def __repr__(self):
#         return f"Event('{self.name}', '{self.date}', '{self.location}')"


class EventSignup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eventnum = db.Column(db.String(100))
    name = db.Column(db.String(100))
    age = db.Column(db.Integer())
    phone = db.Column(db.String(20))
    email = db.Column(db.String(150))
    time = db.Column(db.String(100))
    introduction = db.Column(db.String(500))
    # event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

    def __repr__(self):
        return f"EventSignup('{self.eventnum}','{self.name}', '{self.age}', '{self.phone}', '{self.email}', '{self.time}', '{self.introduction}')"
