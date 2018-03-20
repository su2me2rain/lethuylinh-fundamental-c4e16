from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds117759.mlab.com:17759/linhc4e16'

#1. connect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. Create collection
music = db['music']
#
# #4. Create a new document
#
# new_music = [
# {
#     'title': 'Dark Horse',
#     'Singer': 'Katty Perry',
# },
# {
#     'title': 'Fireword',
#     'Singer': 'Katty Perry',
# },
# {
#     'title': 'I kissed a girl',
#     'Singer': 'Katty Perry',
# },
# {
#     'title': 'Roar',
#     'Singer': 'Katty Perry',
# },
# {
#     'title': 'Last Friday Night',
#     'Singer': 'Katty Perry',
# }]
#
# #5. Insert document into collection
# for i in range(len(new_music)):
#     music.insert_one(new_music[i])

all_music = music.find()

for music in all_music:
    print(music['title'])
