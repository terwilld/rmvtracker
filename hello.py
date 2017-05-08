import os
import sys
from flask import Flask, render_template, request, url_for, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import psycopg2
import urlparse
from subprocess import Popen, PIPE
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
    print '<local test> DB_name: ', DB_name
    print '<local test> DB_user: ', DB_user
    print '<local test> DB_password: ', DB_password
    print '<local test> DB_host: ', DB_host
    print '<local test> DB_port: ', DB_port    
    print 'got config file this must be a local build'
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
    print 'database type : ', type(url.path[1:]), ' Database name: ', str(url.path[1:])
    print 'user type : ', type(url.username), ' User:  ', str(url.username)
    print 'password type: ', type(url.password), ' Password: ', str(url.password)
    print 'host type : ', type (url.hostname), ' Host: ', str(url.hostname)
    print 'port type: ', type(url.port), ' Port: ', str(url.port)




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
    print "print test 2"
    sys.stdout.flush()
    return 'shit'






#http://neillobo.azurewebsites.net/setting-up-postgres-on-heroku/
@app.route("/test2")
def test2():
    try:
        print 'got in'
        conn = psycopg2.connect(
         database=DB_name,
         user=DB_user,
         password=DB_password,
         host=DB_host,
         port=DB_port,
         sslmode='require'
        )
        print 'made connection'
      
      #cur is the cursor which is used to execute all PSQL queries

        cur = conn.cursor()
        try:
            print 'test inside try make table'

            cur.execute("CREATE TABLE test_1 (id serial PRIMARY KEY, num integer, data varchar);")
            print 'made table'
        except:
            return 'failed'
        conn.commit()
        print 'commited'



    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)
        sys.exit(1)


    if conn != None:
        output = "Connected to database successfully!\n"
        conn.close()
    return "Hello World"+output


@app.route("/test3")
def test3():
    try:
        print 'got in'
        conn = psycopg2.connect(
         database=DB_name,
         user=DB_user,
         password=DB_password,
         host=DB_host,
         port=DB_port,
         sslmode='require'
        )
        print 'made connection'
        cur = conn.cursor()
        try:
            print 'test inside try make table'
            cur.execute("CREATE TABLE test_2 (id serial PRIMARY KEY, num integer, data varchar);")

            cur.execute("CREATE TABLE Current_Data(Date_time VARCHAR(35),\
        Attleboro_Licensing INT, Attleboro_Registration INT, \
        Boston_Licensing INT, Boston_Registration INT, \
        Braintree_Licensing INT, Braintree_Registration INT, \
        Brockton_Licensing INT, Brockton_Registration INT, \
        Chicopee_Licensing INT, Chicopee_Registration INT, \
        Easthampton_Licensing INT, Easthampton_Registration INT, \
        Fall_River_Licensing INT, Fall_River_Registration INT, \
        Greenfield_Licensing INT, Greenfield_Registration INT, \
        Haverhill_Licensing INT, Haverhill_Registration INT, \
        Lawrence_Licensing INT, Lawrence_Registration INT, \
        Leominster_Licensing INT, Leominster_Registration INT, \
        Lowell_Licensing INT, Lowell_Registration INT, \
        Marthas_Vineyard_Licensing INT, Marthas_Vineyard_Registration INT, \
        Milford_Licensing INT, Milford_Registration INT, \
        Nantucket_Licensing INT, Nantucket_Registration INT, \
        Natick_Licensing INT, Natick_Registration INT, \
        New_Bedford_Licensing INT, New_Bedford_Registration INT, \
        North_Adams_Licensing INT, North_Adams_Registration INT, \
        Pittsfield_Licensing INT, Pittsfield_Registration INT, \
        Plymouth_Licensing INT, Plymouth_Registration INT, \
        Revere_Licensing INT, Revere_Registration INT, \
        Roslindale_Licensing INT, Roslindale_Registration INT, \
        South_Yarmouth_Licensing INT, South_Yarmouth_Registration INT, \
        Springfield_Licensing INT, Springfield_Registration INT, \
        Taunton_Licensing INT, Taunton_Registration INT, \
        Watertown_Licensing INT, Watertown_Registration INT, \
        Wilmington_Licensing INT, Wilmington_Registration INT, \
        Worcester_Licensing INT, Worcester_Registration INT)")


            conn.commit()
            conn.close()
            return 'made table'
            print 'made table'
        except:
            return 'failed to make table'
    except:
        return 'failed to connect'







if __name__ == "__main__":
    app.run(debug=True)
