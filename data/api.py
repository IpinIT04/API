import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
api = Api(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ipin%402004@localhost:5432/postgres'
db = SQLAlchemy(app)


class PersonModel(db.Model):
    id_person = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100))
    gender = db.Column(db.String(10)) 
    job = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    company = db.Column(db.String(100))
    skills = db.Column(db.ARRAY(db.String))

    def __init__(self, name, age, city, gender, job, email, company, skills):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        self.job = job
        self.email = email
        self.company = company
        self.skills = skills


parser = reqparse.RequestParser()
parser.add_argument('id_person', type=int, help='ID of person')
parser.add_argument('name', type=str, help='Name of person')
parser.add_argument('age', type=int, help='Age of person')
parser.add_argument('city', type=str, help='City of person')
parser.add_argument('gender', type=str, help='Gender of person')
parser.add_argument('job', type=str, help='Job of person')
parser.add_argument('email', type=str, help='Email of person')
parser.add_argument('company', type=str, help='Company of person')
parser.add_argument('skills', type=str, action='append', help='Skills of person')


class PersonResource(Resource):
    def get(self):
        people = PersonModel.query.all()
        people_list = []
        
        for person in people:
            people_list.append({
                'id_person': person.id_person,
                'name': person.name,
                'age': person.age,
                'city': person.city,
                'gender': person.gender,
                'job': person.job,
                'email': person.email,
                'company': person.company,
                'skills': person.skills
            })
        return {'people': people_list}, 200
    

    def post(self):
        args = parser.parse_args()

        new_person = PersonModel(
            name=args['name'],
            age=args['age'],
            city=args['city'],
            gender=args['gender'],
            job=args['job'],
            email=args['email'],
            company=args['company'],
            skills=args['skills']
        )
        db.session.add(new_person)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
        return {'message': 'New person added successfully.'}, 201


api.add_resource(PersonResource, '/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='192.168.1.46', port=2112, debug=True)