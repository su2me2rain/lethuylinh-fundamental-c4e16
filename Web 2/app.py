from flask import *
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

@app.route('/admin')
def admin():
    services = Service.objects()
    return render_template('admin.html', services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        return "Not found"
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))

@app.route('/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        gender = form['gender']
        new_service = Service(name=name, yob=yob, address = address, gender = gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>', methods = ['GET','POST'])
def update(service_id):
    service = Service.objects().with_id(service_id)
    if request.method == 'GET':
        return render_template('update-service.html', service = service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        measurement = [form['mea1'], form['mea2'], form['mea3']]
        height = form['height']
        description = [form['des1'], form['des2'], form['des3']]
        phone = form['phone']
        address = form['address']
        # if form['status'] == 1:
        #     status = True
        # else:
        #     status = False
        image = form['image']
        # gender = form['gender']
        service.update(set__name = name,
                            set__yob = yob,
                            set__measurement = measurement,
                            set__height = height,
                            set__description = description,
                            set__phone = phone,
                            set__address = address,
                            # set__status = status,
                            set__image = image,
                            # set__gender = gender
                            )
        service.reload()
        return redirect(url_for('detail', service_id = service_id))

@app.route('/services')
def services():
    all_services = Service.objects()
    return render_template('services.html',all_services = all_services)

@app.route('/detail/<service_id>')
def detail(service_id):
    service_id=Service.objects().with_id(service_id)
    return render_template('detailed_service.html',service_id = service_id)

@app.route('/deleteall')
def deleteall():
    services = Service.objects()
    if services is None:
        return "Folder is empty"
    else:
        for service in services:
                service.delete()
        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
