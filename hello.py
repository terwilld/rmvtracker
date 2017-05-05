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
        print database
        print userprint password
        print host
        print port
        
        print 'test 1234'
        cur = conn.cursor()
        print '2352134'
        #cur.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR age INTEGER);")
        try:

            #cur.execute("CREATE TABLE Current_Data(Date_time VARCHAR(35)")
            cur.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR age INTEGER);")
        except:

            return 'failed'
        print 'made table'
        conn.commit()
        print 'commited'



    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)
        sys.exit(1)


    if conn != None:
        output = "Connected to database successfully!\n"
        conn.close()
    return "Hello World"+output


#dbname = config.MYSQL_DATABASE


if __name__ == "__main__":
    app.run(debug=True)
