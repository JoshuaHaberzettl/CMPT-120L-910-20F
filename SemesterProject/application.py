from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a test.'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/name')
def hello(name='Josh'):
    return render_template('hello.html', name=name)