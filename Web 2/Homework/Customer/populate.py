from models.customer import Customer
import mlab
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()

#create a document
for i in range(100):
    print('running')
    new_customer = Customer(name = fake.name(),
                            gender = randint(0,1),
                            email = fake.email(),
                            phone = fake.phone_number(),
                            job = fake.job(),
                            company = fake.company(),
                            contact = choice([True, False]))
    new_customer.save()
