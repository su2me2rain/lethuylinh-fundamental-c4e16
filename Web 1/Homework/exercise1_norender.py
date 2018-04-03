from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    bmi = weight/((height/100)**2)
    if bmi < 16:
        result = 'Severely underweight'
    elif bmi < 18.5:
        result = 'Underweight'
    elif bmi < 25:
        result ='Normal'
    elif bmi < 30:
        result = 'Overweight'
    else:
        result = 'Obese'
    return result

if __name__ == '__main__':
  app.run(debug=True)
