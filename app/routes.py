from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import UserInfoForm, VisaInfoForm
from app.models import UserInfo, VisaInfo, Purpose, Document, VisaCost
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Function to convert duration strings to days
def convert_duration_to_days(duration):
    if duration == '< 30 days':
        return 30
    elif duration == '30-90 days':
        return 90
    elif duration == '91-180 days':
        return 180
    elif duration == '181-365 days':
        return 365
    elif duration == '> 365 days':
        return 366  # Arbitrary high number for filtering

# Function to convert validity period to days
def convert_validity_to_days(validity_period):
    if 'day' in validity_period:
        return int(validity_period.split()[0])
    elif 'month' in validity_period:
        return int(validity_period.split()[0]) * 30
    elif 'year' in validity_period:
        return int(validity_period.split()[0]) * 365
    return 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_info', methods=['GET', 'POST'])
def submit_info():
    form = UserInfoForm()
    visas = None

    if form.validate_on_submit():
        nationality = form.nationality.data
        destination_country = form.destination_country.data
        purpose_of_visit = form.purpose_of_visit.data
        duration_of_stay = form.duration_of_stay.data
        max_duration_days = convert_duration_to_days(duration_of_stay)

        visas = VisaInfo.query.join(VisaInfo.purposes).filter(
            VisaInfo.nationality == nationality,
            VisaInfo.destination_country == destination_country,
            Purpose.name == purpose_of_visit
        ).all()
        
        visas = [visa for visa in visas if convert_validity_to_days(visa.validity_period) <= max_duration_days]
        
        flash('Filtered visas based on your criteria.')
    return render_template('submit_info.html', title='Submit Information', form=form, visas=visas)

@app.route('/visa_info/<int:visa_id>')
def visa_info(visa_id):
    visa = VisaInfo.query.get_or_404(visa_id)
    purposes = [purpose.name for purpose in visa.purposes]
    documents = [document.name for document in visa.required_documents]
    costs = VisaCost.query.filter_by(visa_id=visa_id).all()
    return render_template('visa_info.html', visa=visa, purposes=purposes, documents=documents, costs=costs)

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

        # Add purposes to the VisaInfo instance
        for purpose_name in form.purposes.data:
            purpose = Purpose.query.filter_by(name=purpose_name).first()
            if not purpose:
                purpose = Purpose(name=purpose_name)
                db.session.add(purpose)
            visa_info.purposes.append(purpose)

        # Add required documents to the VisaInfo instance
        for document_name in form.required_documents.data:
            document = Document.query.filter_by(name=document_name).first()
            if not document:
                document = Document(name=document_name)
                db.session.add(document)
            visa_info.required_documents.append(document)

        db.session.add(visa_info)
        db.session.commit()
        logging.debug('VisaInfo added successfully')

        # Add costs associated with the VisaInfo instance
        for cost_form in form.costs.entries:
            visa_cost = VisaCost(
                visa_id=visa_info.id,
                entry_frequency=cost_form.entry_frequency.data,
                cost=cost_form.cost.data,
                currency=cost_form.currency.data
            )
            db.session.add(visa_cost)
            logging.debug(f'Added visa cost: {cost_form.entry_frequency.data} - {cost_form.cost.data} {cost_form.currency.data}')

        db.session.commit()

        flash('Visa information has been added successfully!')
        return redirect(url_for('add_visa'))
    else:
        logging.error('Form validation failed')
        logging.debug(form.errors)
    return render_template('add_visa.html', title='Add Visa Information', form=form)
