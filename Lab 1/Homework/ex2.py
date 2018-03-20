from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

#1. connect to database
client = MongoClient(mongo_uri)
