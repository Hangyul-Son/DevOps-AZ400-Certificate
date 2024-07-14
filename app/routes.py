from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import UserInfoForm
from app.models import UserInfo
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_info', methods=['GET', 'POST'])
def submit_info():
    form = UserInfoForm()
    if form.validate_on_submit():
        user_info = UserInfo(
            nationality=form.nationality.data,
            destination_country=form.destination_country.data,
            purpose_of_visit=form.purpose_of_visit.data,
            duration_of_stay=form.duration_of_stay.data
        )
        db.session.add(user_info)
        db.session.commit()
        flash('Information submitted successfully!', 'success')
        return redirect(url_for('show_visa_options'))  # Replace 'show_visa_options' with your next route
    return render_template('submit_info.html', title='Submit Information', form=form)
