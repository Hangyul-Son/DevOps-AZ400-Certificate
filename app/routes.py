from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import UserInfoForm, VisaInfoForm
from app.models import UserInfo, VisaInfo, Purpose, Document, VisaCost
import logging

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

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/add_visa', methods=['GET', 'POST'])
def add_visa():
    form = VisaInfoForm()
    if form.validate_on_submit():
        logging.debug('Form validated successfully')
        visa_info = VisaInfo(
            nationality=form.nationality.data,
            destination_country=form.destination_country.data,
            visa_type=form.visa_type.data,
            validity_period=form.validity_period.data,
            processing_time=form.processing_time.data,
            application_method=form.application_method.data
        )
        # Add purposes
        for purpose_name in form.purposes.data:
            purpose = Purpose.query.filter_by(name=purpose_name).first()
            if purpose:
                visa_info.purposes.append(purpose)
                logging.debug(f'Added purpose: {purpose_name}')
            else:
                logging.error(f'Purpose not found: {purpose_name}')
        # Add required documents
        for document_name in form.required_documents.data:
            document = Document.query.filter_by(name=document_name).first()
            if document:
                visa_info.required_documents.append(document)
                logging.debug(f'Added document: {document_name}')
            else:
                logging.error(f'Document not found: {document_name}')
        db.session.add(visa_info)
        db.session.commit()
        logging.debug('VisaInfo added successfully')
        # Add costs
        for cost_form in form.costs.entries:
            visa_cost = VisaCost(
                visa_id=visa_info.id,
                entry_frequency=cost_form.form.entry_frequency.data,
                cost=cost_form.form.cost.data,
                currency=cost_form.form.currency.data
            )
            db.session.add(visa_cost)
            logging.debug(f'Added visa cost: {cost_form.form.entry_frequency.data} - {cost_form.form.cost.data} {cost_form.form.currency.data}')
        db.session.commit()
        flash('Visa information has been added successfully!')
        return redirect(url_for('add_visa'))
    else:
        logging.error('Form validation failed')
    return render_template('add_visa.html', title='Add Visa Information', form=form)


