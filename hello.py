import os
from flask import Flask, render_template, request, url_for

#need forms likbrary




app = Flask(__name__)

@app.route("/base")
def base():
    return render_template('base.html')
#	return render_template('hello.html')


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

@app.route("/programming/blog/nav_test")
def nav_test():
        return render_template('/programming/blog/nav_test.html')
@app.route("/programming/blog/nav_test_2")
def nav_test_2():
        return render_template('/programming/blog/nav_test_2.html')

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



        ##  Cooking
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




if __name__ == "__main__":
    app.run(debug=True)
