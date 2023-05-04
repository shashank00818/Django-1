from faker import Faker
from app1.models import Person
import random


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
                gender=random.choice(["M", "F", "O"]),
                email=fake.email(),
            )
            print(person_obj)
        
        
obj = PopulatePersons()
obj.run()