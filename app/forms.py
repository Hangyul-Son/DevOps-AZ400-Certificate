from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SelectMultipleField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class UserInfoForm(FlaskForm):
    countries = [("South Korea", "South Korea"), ("Vietnam", "Vietnam")]  # Add more countries as needed
    durations = [
        ('< 30 days', 'Less than 30 days'), 
        ('30-90 days', '30-90 days'), 
        ('91-180 days', '91-180 days'), 
        ('181-365 days', '181-365 days'),
        ('> 365 days', 'More than 365 days')
    ]
    purposes = [("Travel", "Travel"), ("Business", "Business")]

    nationality = SelectField('Nationality', choices=countries, validators=[DataRequired()])
    destination_country = SelectField('Destination Country', choices=countries, validators=[DataRequired()])
    purpose_of_visit = SelectField('Purpose of Visit', choices=purposes)
    duration_of_stay = SelectField('Duration of Stay', choices=durations)
    submit = SubmitField('Submit')

class VisaCostForm(FlaskForm):
    entry_frequency = SelectField('Entry Frequency', choices=[('Single Entry', 'Single Entry'), ('Multiple Entry', 'Multiple Entry')], validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    currency = SelectField('Currency', choices=[('USD', 'USD'), ('VND', 'VND'), ('EUR', 'EUR')], validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SelectMultipleField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class VisaCostForm(FlaskForm):
    entry_frequency = SelectField('Entry Frequency', choices=[('Single Entry', 'Single Entry'), ('Multiple Entry', 'Multiple Entry')], validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    currency = SelectField('Currency', choices=[('USD', 'USD'), ('VND', 'VND'), ('EUR', 'EUR')], validators=[DataRequired()])

class VisaInfoForm(FlaskForm):
    nationality = StringField('Nationality', validators=[DataRequired(), Length(max=64)])
    destination_country = StringField('Destination Country', validators=[DataRequired(), Length(max=64)])
    visa_type = StringField('Visa Type', validators=[Optional(), Length(max=64)])
    validity_period = StringField('Validity Period', validators=[Optional(), Length(max=64)])
    processing_time = StringField('Processing Time', validators=[Optional(), Length(max=64)])
    application_method = SelectField('Application Method', choices=[('Visit Embassy', 'Visit Embassy'), ('Online', 'Online'), ('Visa on Arrival', 'Visa on Arrival')], validators=[Optional()])
    purposes = SelectMultipleField('Purpose', choices=[('Business', 'Business'), ('Travel', 'Travel'), ('Education', 'Education')], validators=[Optional()])
    required_documents = SelectMultipleField('Required Documents', choices=[('Passport', 'Passport'), ('Photo', 'Photo'), ('Application Form', 'Application Form')], validators=[Optional()])
    costs = FieldList(FormField(VisaCostForm), min_entries=1, max_entries=2)
    submit = SubmitField('Submit')
