from flask import Flask, request
from flask import render_template
import logging
app = Flask(__name__)
app.logger.setLevel(logging.INFO)


#home page
@app.route('/')
def hello_world():
    app.logger.info('Home page')
    return render_template('home.html')

#Contact page
@app.route('/contacts')
def contacts():
    app.logger.info('Contact page')
    return render_template('contacts.html')

#about me page
@app.route('/aboutMe')
def about_me():
    app.logger.info('About me page')
    return render_template('aboutMe.html')

#nothing page
@app.route('/nothing')
def nothing():
    app.logger.info('A page of no significance')
    return render_template('nothing.html')


#404 page
@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning('404 Page does not exist')
    return render_template('pageNotFound.html'), 404