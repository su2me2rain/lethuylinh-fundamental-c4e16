from models.service import Service
import mlab

mlab.connect()

# all_services = Service.objects()
# print(all_services[6].name)
# all_services = Service.objects().first()
id_to_find = '5ac08e958e925e1e746ebf7c'

# id = Service.objects(id=id_to_find)[0]
id = Service.objects.with_id(id_to_find)
if id is None:
    print('Service not found')
else:
    # print(id.to_mongo())
    # id.delete()
    # print('Deleted')
    id.update(set__yob = 2000)
    id.reload()
    print(id.yob)
