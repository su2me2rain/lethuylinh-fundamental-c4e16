
from mongoengine import *
import mlab

#create collection
#design database
class Customer(Document):
    name = StringField()
    gender = IntField() # 0: female, 1: male
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contact = BooleanField() # True: Contacted, False: Not yet contacted
