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


if __name__ == "__main__":
    app.run(debug=True)
