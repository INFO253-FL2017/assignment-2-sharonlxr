"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"
@app.route('/blog/8-experiments-in-motivation')
def exper():
	return render_template("8ExperimentsinMotivation.html")

@app.route('/contact')
def contact():
	return render_template("contact_us.html")
@app.route('/index')
def index():
	return render_template("index.html")
@app.route('/about')
def about():
	return render_template("about_us.html")
@app.route('/blog/a-mindful-shift-of-focus')
def mind():
	return render_template("AMindfulShiftofFocus.html")
@app.route("/blog/how-to-develop-an-awesome-sense-of-direction")
def how():
	return render_template("HowtoDevelopanAwesomeSenseofDirection.html")
@app.route("/blog/training-to-be-a-good-writer")
def train():
	return render_template("TrainingtoBeaGoodWriter.html")
@app.route("/blog/what-productivity-systems-wont-solve")
def what():
	return render_template("WhatProductivitySystemsWon'tSolve.html")
@app.route("/contact",methods=['POST'])
def send():
	name = request.form.get("name")
	message = request.form.get("message")
	subject = request.form.get("subject")
	
	return render_template("index.html")
# @app.route('/contact_us',methods=['POST'])
# def con():
# 	name = request.form.get("name")
# 	message = request.form.get("message")
# 	subject = request.form.get("subject")
# 	if len(name)==0 or len(message) ==0 or len(subject)==0:
# 		return

