import random

names = ['Peter', 'Alise', 'John', 'Maria', 'Sophia', 'James', 'Lucas', 'Ella', 'Liam', 'Emma']
ages = range(20, 50)
cities = ['Toronto', 'New York', 'London', 'Paris', 'Berlin', 'Sydney', 'Tokyo', 'Shanghai', 'Moscow', 'Dubai']
genders = ['Male', 'Female', 'Other']
jobs = ['Recruiter', 'Engineer', 'Teacher', 'Artist', 'Scientist', 'Doctor', 'Nurse', 'Lawyer', 'Architect', 'Chef']
emails = ['gmail.com', 'yahoo.com', 'outlook.com', 'icloud.com']
companies = ['Google', 'Amazon', 'Microsoft', 'Facebook', 'Tesla', 'Uber', 'Netflix', 'Airbnb', 'Spotify', 'Adobe']
skills_list = ['Python', 'Java', 'C++', 'SQL', 'Data Analysis', 'Machine Learning', 'Communication', 'Leadership']


id_person = 1

def generate_data():
    global id_person
    name = random.choice(names)
    age = random.choice(ages)
    city = random.choice(cities)
    gender = random.choice(genders)
    job = random.choice(jobs)
    email = f'{name.lower()}.{random.randint(1, 100)}@{random.choice(emails)}'
    company = random.choice(companies)
    skills = random.sample(skills_list, random.randint(1, 3))

    record = {'id_person': id_person, 'name': name, 'age': age, 'city': city, 'gender': gender, 'job': job, 'email': email, 'company': company, 'skills': skills}

    id_person += 1

    return record


data_source = (generate_data() for _ in range(5000))   
