from app import db

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(64), nullable=False)
    destination_country = db.Column(db.String(64), nullable=False)
    purpose_of_visit = db.Column(db.String(64), nullable=True)
    duration_of_stay = db.Column(db.String(64), nullable=True)

# Tag models for purposes and documents
class Purpose(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

# Join tables for many-to-many relationships
visa_purpose = db.Table('visa_purpose',
    db.Column('visa_id', db.Integer, db.ForeignKey('visa_info.id'), primary_key=True),
    db.Column('purpose_id', db.Integer, db.ForeignKey('purpose.id'), primary_key=True)
)

visa_document = db.Table('visa_document',
    db.Column('visa_id', db.Integer, db.ForeignKey('visa_info.id'), primary_key=True),
    db.Column('document_id', db.Integer, db.ForeignKey('document.id'), primary_key=True)
)

# VisaCost model
class VisaCost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visa_id = db.Column(db.Integer, db.ForeignKey('visa_info.id'), nullable=False)
    entry_frequency = db.Column(db.String(64), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)

# Visa information table
class VisaInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(64), nullable=False)
    destination_country = db.Column(db.String(64), nullable=False)
    visa_type = db.Column(db.String(64), nullable=True)
    validity_period = db.Column(db.String(64), nullable=True)
    processing_time = db.Column(db.String(64), nullable=True)
    application_method = db.Column(db.String(64), nullable=True)
    purposes = db.relationship('Purpose', secondary=visa_purpose, lazy='subquery',
                               backref=db.backref('visas', lazy=True))
    required_documents = db.relationship('Document', secondary=visa_document, lazy='subquery',
                                         backref=db.backref('visas', lazy=True))
    costs = db.relationship('VisaCost', backref='visa', lazy=True)

    def __repr__(self):
        return f'<VisaInfo {self.visa_type} to {self.destination_country}>'


    def __repr__(self):
        return f'<VisaInfo {self.visa_type} to {self.destination_country}>'
