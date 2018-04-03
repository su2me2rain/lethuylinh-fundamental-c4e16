from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts =[
        {
            'title': 'A',
            'content': 'lalala',
            'gender': 1,
            'author': 'Linh'
        },
        {
            'title': 'B',
            'content': 'hihihi',
            'gender': 0,
            'author': 'Linh Thùy'
        }
    ]
    return render_template('index.html', posts = posts)

@app.route('/hello')
def hello():
    return 'Hello C4E 16'

@app.route('/sayhi/<name>/<age>')
def sayhi(name, age):
    return 'Hi ' + name + ". You're " + age + ' years old.'

@app.route('/sum/<int:x>/<int:y>')
def calc(x, y):
    # k = int(x) + int(y)
    # return x + ' + ' + y + ' = ' + str(k)
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
