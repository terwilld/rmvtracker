import os
import sys
from flask import Flask, render_template, request, url_for, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import psycopg2
import urlparse





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
        urlparse.uses_netloc.append("postgres")
      #parse the 'DATABASE_URL' variable into url

        url = urlparse.urlparse(os.environ["DATABASE_URL"])


        conn = psycopg2.connect(
         database=url.path[1:],
         user=url.username,
         password=url.password,
         host=url.hostname,
         port=url.port
        )
      #cur is the cursor which is used to execute all PSQL queries
        print 'test 1234'
        cur = conn.cursor()
        print '2352134'
        #cur.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR age INTEGER);")
        cur.execute("CREATE TABLE Current_Data(Date_time VARCHAR(35)")
        print 'made table'
        conn.commit()
        print 'commited'

#try:
#    conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)
        sys.exit(1)
#else:
#   print('Connected!')
   # do stuff










    #https://techarena51.com/blog/flask-sqlalchemy-postgresql-tutorial/
    # cur.execute("CREATE TABLE Current_Data_1(Date_time VARCHAR(35),\
    #     Attleboro_Licensing INT, Attleboro_Registration INT, \
    #     Boston_Licensing INT, Boston_Registration INT, \
    #     Braintree_Licensing INT, Braintree_Registration INT, \
    #     Brockton_Licensing INT, Brockton_Registration INT, \
    #     Chicopee_Licensing INT, Chicopee_Registration INT, \
    #     Easthampton_Licensing INT, Easthampton_Registration INT, \
    #     Fall_River_Licensing INT, Fall_River_Registration INT, \
    #     Greenfield_Licensing INT, Greenfield_Registration INT, \
    #     Haverhill_Licensing INT, Haverhill_Registration INT, \
    #     Lawrence_Licensing INT, Lawrence_Registration INT, \
    #     Leominster_Licensing INT, Leominster_Registration INT, \
    #     Lowell_Licensing INT, Lowell_Registration INT, \
    #     Marthas_Vineyard_Licensing INT, Marthas_Vineyard_Registration INT, \
    #     Milford_Licensing INT, Milford_Registration INT, \
    #     Nantucket_Licensing INT, Nantucket_Registration INT, \
    #     Natick_Licensing INT, Natick_Registration INT, \
    #     New_Bedford_Licensing INT, New_Bedford_Registration INT, \
    #     North_Adams_Licensing INT, North_Adams_Registration INT, \
    #     Pittsfield_Licensing INT, Pittsfield_Registration INT, \
    #     Plymouth_Licensing INT, Plymouth_Registration INT, \
    #     Revere_Licensing INT, Revere_Registration INT, \
    #     Roslindale_Licensing INT, Roslindale_Registration INT, \
    #     South_Yarmouth_Licensing INT, South_Yarmouth_Registration INT, \
    #     Springfield_Licensing INT, Springfield_Registration INT, \
    #     Taunton_Licensing INT, Taunton_Registration INT, \
    #     Watertown_Licensing INT, Watertown_Registration INT, \
    #     Wilmington_Licensing INT, Wilmington_Registration INT, \
    #     Worcester_Licensing INT, Worcester_Registration INT)")
    # conn.commit()




    if conn != None:
        output = "Connected to database successfully!\n"
        conn.close()
    return "Hello World"+output


#dbname = config.MYSQL_DATABASE


if __name__ == "__main__":
    app.run(debug=True)
