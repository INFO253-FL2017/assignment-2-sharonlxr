"""
webserver.py

File that is the central location of code for your webserver.
"""
import os
import requests
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
	result = send_simple_message(name,subject,message)
	print(result.status_code)
	success = "Hi {}, your message has been sent".format(name)
	if result.status_code==200:
		return render_template("contact_us.html",notifications = [success])
	return render_template("contact_us.html")

def send_simple_message(name,subject,message):
	user = os.environ['INFO253_MAILGUN_USER']
	key = os.environ['INFO253_MAILGUN_PASSWORD']
	sender = os.environ['INFO253_MAILGUN_FROM_EMAIL']
	receiver = os.environ['INFO253_MAILGUN_TO_EMAIL']
	domain = os.environ['INFO253_MAILGUN_DOMAIN']
	
	from_add = name+" <"+sender+">"
	to_add = "<"+receiver+">"

	api="https://api.mailgun.net/v3/{}/messages".format(domain)
	infodata={"from": from_add, "to": to_add,"subject": subject,"text": message}
	return requests.post(api,auth=(user,key),data=infodata)
    # return requests.post(api,auth=("api", "key-a17538386618a4b4953619758057e10f"),data={"from": from_add, "to": to_add,"subject": subject,"text": message})