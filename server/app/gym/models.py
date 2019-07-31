import datetime as dt
from app import db
from sqlalchemy import func
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

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get(cls, quicklook):
        return cls.query.filter_by(quicklook=quicklook).first()


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    visitor_id = db.Column(db.String, db.ForeignKey('users.quicklook'), nullable=False)
    visitor = db.relationship('User', foreign_keys='Visit.visitor_id', back_populates='visits')
    datetime = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def count_btw(cls, start, end):
        return cls.query.filter(cls.datetime >= start).filter(cls.datetime <= end).count()

    @classmethod
    def count_by_day(cls, date: dt.date):
        return cls.query.filter(func.date(cls.datetime) == date).count()
