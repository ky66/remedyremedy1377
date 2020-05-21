from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from sqlalchemy import func
from datetime import date


from flask_qa.extensions import db
from flask_qa.models import doctors, patients, history, medication, visits

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        doctor = doctors.query.filter_by(username=name).first()

        if not doctor:
            flash('Could not login. Please try again or register.')
            return redirect(url_for('main.login'))
        elif not check_password_hash(doctor.password, password):
            flash('Password incorrect. Please try again.')
            return redirect(url_for('main.login'))
        else:
            login_user(doctor)
            return redirect(url_for('main.patientsearch'))

    return render_template('login.html')

@main.route('/registerdoctor', methods=['GET', 'POST'])
def registerdoctor():
    if request.method == 'POST':
        name = request.form['name']

        doctor = doctors.query\
        .filter(func.lower(doctors.username)==func.lower(name)).first()

        if not doctor:
            doctor = doctors(
                username=name,
                unhashed_password=request.form['password'],
            )
            try:
                db.session.add(doctor)
                db.session.commit()
                return redirect(url_for('main.login'))
            except:
                flash('Error adding user. Try again later.')

        else:
            flash('User already registered. Login please.')

    return render_template('registerdoctor.html')

@main.route('/clinic', methods=['GET', 'POST'])
@login_required
def clinic():
    return render_template('clinic.html')


@main.route('/trends', methods = ['GET', 'POST'])
def trends():

    context = {

    'zerotofive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-5)) or\
     (((extract(year from dob))=(extract(year from now())-5)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-5)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],


    'fivetoten' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-10) and (extract(year from dob))<(extract(year from now())-5)) or\
     (((extract(year from dob))=(extract(year from now())-5)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-5)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-10)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-10)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'tentofifteen' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-15) and (extract(year from dob))<(extract(year from now())-10)) or\
     (((extract(year from dob))=(extract(year from now())-10)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-10)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-15)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-15)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'fifteentotwenty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-20) and (extract(year from dob))<(extract(year from now())-15)) or\
     (((extract(year from dob))=(extract(year from now())-15)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-15)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-20)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-20)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'twentytotwentyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-25) and (extract(year from dob))<(extract(year from now())-20)) or\
     (((extract(year from dob))=(extract(year from now())-20)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-20)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-25)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-25)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'twentyfivetothirty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-30) and (extract(year from dob))<(extract(year from now())-25)) or\
     (((extract(year from dob))=(extract(year from now())-25)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-25)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-30)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-30)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'thirtytothirtyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-35) and (extract(year from dob))<(extract(year from now())-30)) or\
     (((extract(year from dob))=(extract(year from now())-30)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-30)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-35)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-35)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'thirtyfivetofourty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-40) and (extract(year from dob))<(extract(year from now())-35)) or\
     (((extract(year from dob))=(extract(year from now())-35)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-35)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-40)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-40)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'fourtytofourtyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-45) and (extract(year from dob))<(extract(year from now())-40)) or\
     (((extract(year from dob))=(extract(year from now())-40)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-40)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-45)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-45)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'fourtyfivetofifty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-50) and (extract(year from dob))<(extract(year from now())-45)) or\
     (((extract(year from dob))=(extract(year from now())-45)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-45)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-50)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-50)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'fiftytofiftyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-55) and (extract(year from dob))<(extract(year from now())-50)) or\
     (((extract(year from dob))=(extract(year from now())-50)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-50)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-55)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-55)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'fiftyfivetosixty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-60) and (extract(year from dob))<(extract(year from now())-55)) or\
     (((extract(year from dob))=(extract(year from now())-55)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-55)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-60)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-60)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'sixtytosixtyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-65) and (extract(year from dob))<(extract(year from now())-60)) or\
     (((extract(year from dob))=(extract(year from now())-60)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-60)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-65)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-65)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'sixtyfivetoseventy' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-70) and (extract(year from dob))<(extract(year from now())-65)) or\
     (((extract(year from dob))=(extract(year from now())-65)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-65)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-70)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-70)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'seventytoseventyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-75) and (extract(year from dob))<(extract(year from now())-70)) or\
     (((extract(year from dob))=(extract(year from now())-70)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-70)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-75)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-75)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'seventyfivetoeighty' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-80) and (extract(year from dob))<(extract(year from now())-75)) or\
     (((extract(year from dob))=(extract(year from now())-75)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-75)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-80)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-80)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'eightytoeightyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-85) and (extract(year from dob))<(extract(year from now())-80)) or\
     (((extract(year from dob))=(extract(year from now())-80)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-80)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-85)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-85)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'eightyfivetoninety' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-90) and (extract(year from dob))<(extract(year from now())-85)) or\
     (((extract(year from dob))=(extract(year from now())-85)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-85)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-90)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-90)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'ninetytoninetyfive' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-95) and (extract(year from dob))<(extract(year from now())-90)) or\
     (((extract(year from dob))=(extract(year from now())-90)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-90)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-95)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-95)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],

    'ninetyfivetohundred' : db.session.execute("select count(*) from (select dob from patients) as foo \
    where ((extract(year from dob))>(extract(year from now())-100) and (extract(year from dob))<(extract(year from now())-95)) or\
     (((extract(year from dob))=(extract(year from now())-95)) and ((extract(month from dob))>(extract(month from now())))) or\
     (((extract(year from dob))=(extract(year from now())-95)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))>(extract(day from now()))) or\
     (((extract(year from dob))=(extract(year from now())-100)) and ((extract(month from dob))<(extract(month from now())))) or\
      (((extract(year from dob))=(extract(year from now())-100)) and ((extract(month from dob))=(extract(month from now()))) and (extract(day from dob))<=(extract(day from now())))").first()[0],


      'sun' : db.session.execute("select count(*) from (select dob from patients) as foo where date_part('dow', dob) = 0").first()[0],
      'sun': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 0").first()[0],
      'mon': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 1").first()[0],
      'tue': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 2").first()[0],
      'wed': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 3").first()[0],
      'thur': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 4").first()[0],
      'fri': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 5").first()[0],
      'sat': db.session.execute("select count(*) from (select visitdate from visits) as foo where (date_part('dow', visitdate)) = 6").first()[0],



      'medications' : db.session.execute('select med_name, cast(sum(dose*frequency) as int) as totals from medication where (extract(year from enddate))=(extract(year from now())) group by med_name '),



      }



    return render_template('trends.html', **context)



@main.route('/registerpatient', methods=['GET', 'POST'])
def registerpatient():
    if request.method == 'POST':
        name_first = request.form['name_first']
        name_last = request.form['name_last']
        email = request.form['email']

        patient = patients.query\
        .filter(func.lower(patients.email) == func.lower(email))\
        .filter(func.lower(patients.name_first) == func.lower(name_first))\
        .filter(func.lower(patients.name_last) == func.lower(name_last))\
        .first()

        if patient:
            flash('Patient has already been registered.')

        else:
            patient_obj = patients(
                name_first=name_first,
                name_last=name_last,
                dob=request.form['dob'],
                email=email,
                address=request.form['address'],
                phone=request.form['phone'],
                )

            try:
                db.session.add(patient_obj)
                db.session.commit()
            except:
                flash('Patient could not be registered. Try again later.')
            else:
                flash("Patient successfully registered!")

    return render_template('registerpatient.html')

@main.route('/patientsearch', methods=['GET', 'POST'])
@login_required
def patientsearch():
    context = {
        'patients' : patients.query.all()
    }
    return render_template('patientsearch.html', **context)

@main.route('/patientinfo/<int:patient_id>',  methods=['GET', 'POST'])
@login_required
def patientinfo(patient_id):
    patient_info = patients.query.filter_by(id=patient_id).first()
    if request.method == 'POST':
        try:
            patient_info.dob = request.form['new_dob']
            patient_info.address = request.form['new_add']
            patient_info.email = request.form['new_email']
            patient_info.phone = request.form['new_phone']
            db.session.commit()
        except:
            try:
                medication_obj = medication(
                    patientid=patient_id,
                    med_name = request.form['new_med_name'],
                    dose = request.form['dose'],
                    frequency = request.form['freq'],
                    startdate = request.form['start_date'],
                    enddate= None,
                )
                db.session.add(medication_obj)
                db.session.commit()

            except:
                end_med = medication.query\
                .filter_by(patientid=patient_id)\
                .filter_by(med_name=request.form["end_med"])\
                .filter_by(enddate=None).first()

                end_med.enddate=request.form['end_date']
                db.session.commit()

    context = {
        'patient' : patient_info,
        'history' : history.query.filter_by(patientid=patient_id).first(),
        'current_med' : medication.query\
        .filter_by(patientid=patient_id)\
        .filter_by(enddate=None).all(),
        'all_med' : medication.query.filter_by(patientid=patient_id).all(),
        'visits' : visits.query.filter_by(patientid=patient_id).all(),
    }

    return render_template('patientinfo.html', **context)

@main.route('/newvisit/<int:patient_id>',  methods=['GET', 'POST'])
@login_required
def newvisit(patient_id):
    if request.method == 'POST':
        visit_obj = visits(
            patientid=patient_id,
            visitdate=request.form['visitdate'],
            weight=request.form['weight'],
            height=request.form['height'],
            symptoms=request.form['symptoms'],
            diagnostics=request.form['diagnostics'],
            comorbidities=request.form['comorbidities'],
            clinical_progress=request.form['clinical_progress'],
            support_services=request.form['support_services'],
            doctor_name=request.form['doctor_name']
        )

        db.session.add(visit_obj)
        db.session.commit()
        return redirect(url_for('main.patientinfo', patient_id=patient_id))


    context = {
        'patient' : patients.query.filter_by(id=patient_id).first(),
        'history' : history.query.filter_by(patientid=patient_id).first(),
        'current_med' : medication.query\
        .filter_by(patientid=patient_id)\
        .filter_by(enddate=None).all(),
        'all_med': medication.query.filter_by(patientid=patient_id).all(),
        'visits' : visits.query.filter_by(patientid=patient_id).all()
    }

    return render_template('newvisit.html',**context)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
