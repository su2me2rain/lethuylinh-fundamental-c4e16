from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

#1. connect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. Count data
customers = db.customers.find()
ads = 0
wom = 0
events = 0
for customer in customers:
    if customer['ref'] == 'ads':
        ads += 1
    elif customer['ref'] == 'wom':
        wom +=1
    else:
        events +=1
total = ads + wom + events
pads = ads/total
pwom = wom/total
pevents = events/total

#4. Draw Plot
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

labels = ['Advertisements','Word of Mouth','Events']
values = [pads, pwom, pevents]

pyplot.pie(values,
        labels=labels,
        autopct='%.2f%%'
        )
pyplot.axis('equal')

pyplot.show()
