from faker import Faker
from app1.models import Person
import random

# exec(open('./my_app2/dbscripts/populate_persons.py').read())
# code to run this file in shell

class PopulatePersons:

    def __init__(self):
        pass

    def run(self):
        fake = Faker()
        LIMIT = 10**3
        for i in range(LIMIT):
            person_obj = Person.objects.create(
                fname=fake.first_name(),
                lname=fake.last_name(),
                age=random.randrange(1, 99),
                gender=random.choice([Person.GENDER.male, Person.GENDER.female, Person.GENDER.others]),
                email=fake.email(),
            )
            print(person_obj)

        
obj = PopulatePersons()
obj.run()