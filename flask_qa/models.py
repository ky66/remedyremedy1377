from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db

class doctors(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class patients(db.Model):




    id = db.Column(db.Integer, primary_key = True)
    name_first = db.Column(db.String(50))
    name_last = db.Column(db.String(50))
    dob = db.Column(db.Text)
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    phone = db.Column(db.String(50))

    hasHistory = db.relationship(
        'history',
        foreign_keys='history.patientid',
        lazy = True
    )

    hasMeds = db.relationship(
        'medication',
        foreign_keys='medication.patientid',
        lazy = True
    )

    forPatient = db.relationship(
        'visits',
        foreign_keys='visits.patientid',
        lazy = True
    )

class history(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    patientid = db.Column(db.Integer, db.ForeignKey('patients.id'))
    medical_history = db.Column(db.Text)
    treatment = db.Column(db.Text)


class medication(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    patientid = db.Column(db.Integer, db.ForeignKey('patients.id'))
    med_name = db.Column(db.String(100))
    dose = db.Column(db.Float)
    frequency = db.Column(db.Float)
    startdate = db.Column(db.Text)
    enddate = db.Column(db.Text)


class visits(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    visitdate = db.Column(db.Text)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    symptoms = db.Column(db.Text)
    diagnostics = db.Column(db.Text)
    comorbidities = db.Column(db.Text)
    treatment = db.Column(db.Text)
    doctor_name = db.Column(db.Text)
    patientid = db.Column(db.Integer, db.ForeignKey('patients.id'))
    clinical_progress = db.Column(db.Text)
    support_services = db.Column(db.Text)
