from flask import Flask, request
from flask import render_template
import logging
app = Flask(__name__)
app.logger.setLevel(logging.INFO)


#default page
@app.route('/')
def hello_world():
    app.logger.info('Default test page')
    return render_template('default.html')

#page w/ special url, says hello and can take a name from the url
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.info('Page with url extention')
    return render_template('hello.html', name=name)
