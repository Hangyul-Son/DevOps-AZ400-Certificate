from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class UserInfoForm(FlaskForm):
    countries = [("South Korea", "South Korea"), ("Vietnam", "Vietnam")]  # Add more countries as needed
    durations = [
        ("less_than_1_month", "Less than 1 month"),
        ("1_to_3_months", "More than 1 month, less than 3 months"),
        ("3_to_12_months", "More than 3 months, less than 1 year"),
        ("more_than_1_year", "More than 1 year")
    ]
    purposes = [("Travel", "Travel"), ("Business", "Business")]

    nationality = SelectField('Nationality', choices=countries, validators=[DataRequired()])
    destination_country = SelectField('Destination Country', choices=countries, validators=[DataRequired()])
    purpose_of_visit = SelectField('Purpose of Visit', choices=purposes)
    duration_of_stay = SelectField('Duration of Stay', choices=durations)
    submit = SubmitField('Submit')
