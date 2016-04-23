from flask import Flask, render_template, session, request

app = Flask(__name__)


@app.route('/')
def index_page():

    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form", methods = ['GET', 'POST'])
def application_form():

	"""This will be the application form where users will enter information in the application."""

	applicant_first_name = request.args.get("firstname")
	applicant_last_name = request.args.get("lastname")
	applicant_des_position = request.args.get("desiredposition")
	applicant_des_salary = request.args.get("desiredsalary")

	return render_template("application-form.html", 
							firstname = applicant_first_name, 
							lastname = applicant_last_name, 
							desiredposition = applicant_des_position, 
							desiredsalary = applicant_des_salary)


@app.route("/application-response", methods = ['GET', 'POST'])
def application_response():

	"""This will handle the submissions from appliaction-form.html"""

	return render_template("application-response.html")


@app.route("/about")
def about():

	"""This will handle the submissions from appliaction-form.html"""

	return render_template("about.html")
	#print "Thank you %s, for applying to be a %s. Your minimum salary requirement is %s." %(first_and_last_name, position, salary)

if __name__ == "__main__":
    app.run(debug=True)
