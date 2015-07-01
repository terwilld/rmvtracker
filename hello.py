import os
from flask import Flask, render_template, request, url_for, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
#need forms likbrary
#
mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'terwilld@gmail.com'
app.config["MAIL_PASSWORD"] = 'Brunodog1'

mail.init_app(app)

@app.route("/base")
def base():
    return render_template('base.html')
#	return render_template('hello.html')
#
#
@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
#	return "hello all"
	return render_template('index.html')

@app.route("/nav")
def nav():
        return render_template('nav.html')
@app.route("/navtest")
def navtest():
        return render_template('index.html')

@app.route("/first_landing")
def first_landing():
	return render_template('/first_attempt/landing.html')

@app.route("/first_base")
def first_base():
	return render_template('/first_attempt/base.html')

@app.route("/programming")
def programming():
        return render_template('programming/programming.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Programming/tron-tron_00297189.jpg',
        title='Programming Interests',
        date='A place of tinkering')

            ##  Programming/blog
            ##
@app.route("/programming/blog")
def blog():
        return render_template('programming/blog/blog_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/adobe-photoshop-2014-logo.jpg',
        title='Blog Log',
        date='A haphazard explanation of how this abomination was created')

@app.route("/programming/blog/hello_world")
def programming_blog_hello_world():
        return render_template('/programming/blog/hello_world.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/post-bg.jpg',
        title='A very inefficient, long winded \"Hello World!\"',
        date='December 18, 2014')

@app.route("/programming/blog/part_2")
def programming_blog_part_2():
        return render_template('/programming/blog/part_2.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/post-bg.jpg',
        title='Housekeeping Flavicon and Nav bar',
        date='January 1, 2015')

@app.route("/programming/blog/part_3")
def programming_blog_part_3():
        return render_template('/programming/blog/part_3.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Programming/tron-tron_00297189.jpg',
        title='Template Building',
        date='January 7, 2015')

@app.route("/programming/blog/treehouse_for_xmass")
def treehouse_for_xmass():
        return render_template('/programming/blog/treehouse_for_xmass.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/Screenshot+2014-12-26+10.58.43.png',
        title='A Different Kind of Treehouse for Xmass!',
        date='December 26, 2014')

@app.route("/programming/cronjob_heroku")
def cronjob_heroku():
        return render_template('/programming/cronjob.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Programming/crontab/wallaper-background-files-linux-format-wallpapers_for_desktop.jpg',
        title='UX Cronjob to keep a heroku app running',
        date='March 10, 2015')




@app.route("/programming/blog/nav_test")
def nav_test():
        return render_template('/programming/blog/nav_test.html')
@app.route("/programming/blog/nav_test_2")
def nav_test_2():
        return render_template('/programming/blog/nav_test_2.html')



        #Triathlon scraping article part I
@app.route("/programming/triathlon_scraping_part_I")
def triathlon_scraping_part_I():
    return render_template('/programming/triathlon_scraping.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Programming/triathlon_scraping_part_I/hackers-3.jpg',
        title='Triathlon Result Web-scraping in Python',
        date='June 24, 2015')





            ##  Programming/projects
            ##
@app.route("/programming/projects")
def projects():
    return render_template('programming/projects/projects_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/Screenshot+2014-12-26+10.58.43.png',
        title='Programming Projects',
        date='A few things I\'m working on')

            ##  Programming/puzzles
            ##
@app.route("/programming/puzzles")
def puzzles():
    return render_template('programming/puzzles/puzzles_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/first_pics/Screenshot+2014-12-26+10.58.43.png',
        title='Programming Puzzles',
        date='Playing with programming and Algorithm Design')


        ##  Triathlon 
        ##
        ##
@app.route("/triathlon")
def triathlon():
    return render_template('triathlon/triathlon_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Triathlon/kienle+bike.jpg',
        title='Triathlon',
        date='Thoughts of a middle of the pack age grouper')

@app.route("/triathlon/addpower")
def add_power():
    return render_template('triathlon/add_power.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Triathlon/bike_trainer.jpg',
        title='.TCX editing with Python',
        date='.TCX customization / spoofing with simple scripts.')


@app.route("/triathlon/training_log")
def training_log():
    return render_template('triathlon/training_log.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Triathlon/kienle+bike.jpg',
        title='Triathlon',
        date='Thoughts of a middle of the pack age grouper')

@app.route("/triathlon/bike_fit")
def bike_fit():
    return render_template('triathlon/bike_fit.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Triathlon/bike_fit/output.jpg',
        title='Bike Fit',
        date='An attempt to fit myself to new bike')

        ##  Cooking  s
        ##
        ##
@app.route("/cooking")
def cooking():
    return render_template('cooking/cooking_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Cooking/Cooking.jpg',
        title='Cooking',
        date='Musing of a person trying not to poison himself')

        ##  Reading
        ##
        ##

@app.route("/reading")
def reading():
    return render_template('reading/reading_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Reading/reading.jpg',
        title='Reading',
        date='Interests are primarily Sci-fi and Economics')


@app.route("/misc")
def misc():
    return render_template('misc/misc_index.html',
        background_img='https://s3-us-west-2.amazonaws.com/david-website/Misc/misc.jpg',
        title='Misc',
        date='Random stuff that simply doesn\'t belong anywhere else')


        ##  Contact and formcreation
        ##

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form, title='About / Email', date =' ', background_img='https://s3-us-west-2.amazonaws.com/david-website/Contact/contactus-background-right.jpg')
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['terwilld@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return render_template('contact.html', success=True, title='About / Email', date =' ', background_img='https://s3-us-west-2.amazonaws.com/david-website/Contact/contactus-background-right.jpg')
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form, title='About / Email', date =' ', background_img='https://s3-us-west-2.amazonaws.com/david-website/Contact/contactus-background-right.jpg')






if __name__ == "__main__":
    app.run(debug=True)
