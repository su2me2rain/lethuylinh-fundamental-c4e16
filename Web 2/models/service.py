
from mongoengine import *
import mlab

#create collection
#design database
class Service(Document):
    name = StringField()
    image = StringField()
    description = ListField(StringField(), default=list)
    measurement = ListField(IntField(), default=list)
    yob = IntField()
    gender = IntField() # 0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
