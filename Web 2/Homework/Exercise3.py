from models.service import Service
import mlab

mlab.connect()

id_to_find = "5ac08f1b8e925e1bd0dc8d8a"

#delete the document
Service.objects.get(id = id_to_find).delete()
