from flask import Flask
from flask import render_template
from flask.logging import create_logger
app = Flask(__name__)
logging = create_logger(app)


@app.route('/')
def hello_world():
    logging.info('default test page')
    return 'This is a test.'


@app.route('/hello/')
@app.route('/hello/name')
def hello(name='Josh'):
    logging.info('page with url extention to test templates')
    return render_template('hello.html', name=name)

#example log calls
logging.debug('A value for debugging')
logging.warning('A warning occurred (%d apples)', 42)
logging.error('An error occurred')