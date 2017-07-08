import os
import sys
from flask import Flask, render_template, request, url_for, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import psycopg2
import urlparse
from subprocess import Popen, PIPE
import time
from scrape_locations import *



try:
    print 'Config imported:  Local build'
    from config import * 
    stdout = Popen('heroku config:get DATABASE_URL -a rmv-scraping', shell=True, stdout=PIPE).stdout
    DATABASE_URL = stdout.read()
    urlparse.uses_netloc.append("postgres")
    url=urlparse.urlparse(DATABASE_URL)
    DB_name = url.path[1:]
    DB_user = url.username
    DB_password = url.password
    DB_host = url.hostname
    DB_port = url.port
    DB_name=DB_name[:-1]    #not even a little sure why this is needed, but there was a phantom /n
    # print '<local test> DB_name: ', DB_name
    # print '<local test> DB_user: ', DB_user
    # print '<local test> DB_password: ', DB_password
    # print '<local test> DB_host: ', DB_host
    # print '<local test> DB_port: ', DB_port    
    # print 'got config file this must be a local build'
except:
    print 'no config imported: this is a deployed build'
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])
    DB_name = url.path[1:]
    DB_user = url.username
    DB_password = url.password
    DB_host = url.hostname
    DB_port = url.port
    print '<not inside local test> DB_name: ', DB_name
    print '<not inside local test> DB_user: ', DB_user
    print '<not inside local test> DB_password: ', DB_password
    print '<not inside local test> DB_host: ', DB_host
    print '<not inside local test> DB_port: ', DB_port
    # print 'database type : ', type(url.path[1:]), ' Database name: ', str(url.path[1:])
    # print 'user type : ', type(url.username), ' User:  ', str(url.username)
    # print 'password type: ', type(url.password), ' Password: ', str(url.password)
    # print 'host type : ', type (url.hostname), ' Host: ', str(url.hostname)
    # print 'port type: ', type(url.port), ' Port: ', str(url.port)




mail = Mail()
app = Flask(__name__)
app.secret_key = 'development key'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'terwilld@gmail.com'
app.config["MAIL_PASSWORD"] = 'incorrect'
mail.init_app(app)
@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/base_2")
@app.route("/home")
@app.route("/index")
@app.route("/")
def base_2():
    return render_template('index.html')


@app.route("/how_this_was_made")
def how_this_was_made():
    print "print test 2"
    sys.stdout.flush()
    return render_template('how_this_was_made.html')


@app.route("/test")
def test():
    return DB_name+' '+DB_user+' '+DB_password+' '+str(DB_host)+' '+str(DB_port)






if __name__ == "__main__":
    app.run(debug=True)
