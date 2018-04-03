from flask import Flask, render_template
from models.customer import Customer
import mlab

app = Flask(__name__)
mlab.connect()

@app.route('/')
def index():
    customer = Customer.objects(gender = 1, contact = False)[:10]
    return render_template('index.html', customer = customer)

@app.route('/customer')
def customer():
    customer = Customer.objects()
    return render_template('customer.html', customer = customer)

if __name__ == '__main__':
  app.run(debug=True)
