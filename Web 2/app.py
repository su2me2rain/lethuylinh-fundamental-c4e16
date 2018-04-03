from flask import Flask, render_template
from models.service import Service
import mlab

app = Flask(__name__)
mlab.connect()

#  create a document
# new_service = Service(name = "Trang",
#                         yob = 1991,
#                         gender = 0,
#                         height = 160,
#                         phone = "0936353351",
#                         address = "Ha Noi",
#                         status = False)
# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    # all_services = Service.objects(gender = gender)
    # kieu_anh = all_services[4]
    # return render_template('search.html', all_services = all_services)
    all_services = Service.objects(gender=gender, yob__lte = 1998, address__icontains = 'Ha Noi')
    return render_template('search.html', all_services = all_services)

if __name__ == '__main__':
  app.run(debug=True)
