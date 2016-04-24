from flask import Flask, render_template, session, request, flash
from django.forms import ValidationError

app = Flask(__name__)


@app.route('/')
def index_page():

    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form", methods = ['GET', 'POST'])
def application_form():

	"""This will be the application form where users will enter information in the application."""

	return render_template("application-form.html")


@app.route('/application-response', methods = ['GET', 'POST'])
def greet_person():
	"""This will handle the submissions from appliaction-form.html"""

	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	desiredposition = request.form.get("desiredposition")
	desiredsalary = request.form.get("desiredsalary")

    	return render_template("application-response.html", 
							firstname = firstname, 
							lastname = lastname, 
							desiredposition = desiredposition, 
							desiredsalary = desiredsalary)


@app.route("/about")
def about():

	"""This will handle the submissions from appliaction-form.html"""

	return render_template("about.html")

@app.route("/products")
def products():

	"""This will show a list of our products"""

	return render_template("products.html")

@app.route("/storelocator")
def storelocator():

	"""This will display a map"""

	return render_template("storelocator.html")

if __name__ == "__main__":
    app.run(debug=True)
