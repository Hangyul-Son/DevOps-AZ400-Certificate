from app import db

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(64), nullable=False)
    destination_country = db.Column(db.String(64), nullable=False)
    purpose_of_visit = db.Column(db.String(64), nullable=True)
    duration_of_stay = db.Column(db.String(64), nullable=True)
