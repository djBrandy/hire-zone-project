from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Employer(db.Model):
    __tablename__ = 'employers_table'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    industry = db.Column(db.string, nullable=False)
    location = db.Column(db.String, nullable=False)
    contact_email = db.Column(db.String, nullable=False)

def __repr__(self):
    return f"Employer with the ID of {self.id}, company name of {self.company_name} and the industry of {self.industry} successfully created."


class JobSeekers(db.MOdel):
    __tablename__ = 'job_seekers_table'


    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Employee with the id of {self.id}, and name of {self.first_name} {self.last_name} successfully created."


class JobSeekersDetails (db.Model):
    __tablename__ = 'job_seekers_details'

    id = db.Column(db.Integer, primary_key=True)
    resume_url = db.Column(db.String, nullable=False)
    skills = db.Column(db.String, nullable=False)
    education_level = db.Column(db.String, nullable=False)
    work_experience = db.Column(db.String, nullable=False)
    desired_salary = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False) 
    portfolio_url =db.Column(db.String, nullable=False)


    def __repr__(self):
        return "Employees details added successfully."






