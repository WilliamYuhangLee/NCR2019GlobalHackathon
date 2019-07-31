import datetime
from app import db
from sqlalchemy.orm import validates


# Database models
class User(db.Model):
    __tablename__ = 'users'
    quicklook = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(50))
    visits = db.relationship('Visit', back_populates='visitor')

    @validates('quicklook')
    def validate_quicklook(self, key, value):
        import re
        pattern = re.compile("[a-z]{2}[0-9]{6}")
        assert pattern.match(value)
        return value


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.String, db.ForeignKey('users.quicklook'), nullable=False)
    visitor = db.relationship('User', back_populates='visits')
    datetime = db.Column(db.Date, nullable=False, default=datetime.datetime.utcnow)
