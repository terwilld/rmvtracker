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
        conn = psycopg2.connect(database=DB_name,user=DB_user,password=DB_password,host=DB_host,port=DB_port,sslmode='require')
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
            print 'made table'
            #return 'made table'
        except:
            return 'failed to make table'
    except:
        return 'failed to connect'






    return 'got the whole way through'







@app.route("/add_data")
def add_data():
    list_of_towns=['Attleboro','Boston','Braintree','Brockton','Chicopee','Easthampton','Fall%20River','Greenfield','Haverhill','Lawrence','Leominster','Lowell','Martha%27s%20Vineyard','Milford','Nantucket','Natick','New%20Bedford','North%20Adams','Pittsfield','Plymouth','Revere','Roslindale','South%20Yarmouth','Springfield','Taunton','Watertown','Wilmington','Worcester']
    Result_List=add_a_reading(list_of_towns)
    print Result_List
    print 'test'

    conn = psycopg2.connect(database=DB_name,user=DB_user,password=DB_password,host=DB_host,port=DB_port,sslmode='require')
    print 'made connection'
    cur = conn.cursor()
    print '10'

    cur.execute("INSERT into Current_data(Date_time, \
        Attleboro_Licensing, Attleboro_Registration, \
        Boston_Licensing, Boston_Registration, \
        Braintree_Licensing, Braintree_Registration, \
        Brockton_Licensing, Brockton_Registration, \
        Chicopee_Licensing, Chicopee_Registration, \
        Easthampton_Licensing, Easthampton_Registration, \
        Fall_River_Licensing, Fall_River_Registration, \
        Greenfield_Licensing, Greenfield_Registration, \
        Haverhill_Licensing, Haverhill_Registration, \
        Lawrence_Licensing, Lawrence_Registration, \
        Leominster_Licensing, Leominster_Registration, \
        Lowell_Licensing, Lowell_Registration, \
        Marthas_Vineyard_Licensing, Marthas_Vineyard_Registration, \
        Milford_Licensing, Milford_Registration, \
        Nantucket_Licensing, Nantucket_Registration, \
        Natick_Licensing, Natick_Registration, \
        New_Bedford_Licensing, New_Bedford_Registration, \
        North_Adams_Licensing, North_Adams_Registration, \
        Pittsfield_Licensing, Pittsfield_Registration, \
        Plymouth_Licensing, Plymouth_Registration, \
        Revere_Licensing, Revere_Registration, \
        Roslindale_Licensing, Roslindale_Registration, \
        South_Yarmouth_Licensing, South_Yarmouth_Registration, \
        Springfield_Licensing, Springfield_Registration, \
        Taunton_Licensing, Taunton_Registration, \
        Watertown_Licensing, Watertown_Registration, \
        Wilmington_Licensing, Wilmington_Registration, \
        Worcester_Licensing, Worcester_Registration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)", Result_List)
    print'asdf'
    conn.commit()
    conn.close()





    return 'some data'




if __name__ == "__main__":
    app.run(debug=True)
