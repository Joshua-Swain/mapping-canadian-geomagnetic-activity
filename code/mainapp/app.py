from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from backend_implementation.kriging import Kriging
from backend_implementation.full_data import FullData
from backend_implementation.holed_data import HoledData
from backend_implementation.user_input import UserInput

# Create global variables to store the contents of the dataset
full_data = None
holed_data = None

app = Flask(__name__, static_url_path='')
CORS(app)

@app.before_first_request

# Load the datasets before the very first user request and have it available during the entire lifespan of the application.
# Hence, time taken for file I/O is reduced as the csv files (i.e datasets) are only read once and not for every user request.

def load_datasets():
	print("I am loading datasets")
	global full_data
	full_data = FullData()

	global holed_data
	holed_data = HoledData()



@app.route('/init', methods=['GET'])
def init():
    # "test method"
    return "Init method called"


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

@app.route('/magnetic-field-canada', methods=['POST', 'GET'])
def home(day='01', hour='01', dataset='full'): 
	# Runs on initialization and renders index.html
	if request.method == 'GET':
		print(f"GET request: {day, hour, dataset}", flush=True)
	elif request.method == 'POST':
		form_values = request.form.to_dict()
		day = form_values['day']
		hour = form_values['hour']
		dataset = form_values['dataset']
		print(f"POST request: {day, hour, dataset}", flush=True)

	user_input = UserInput(day, hour, dataset)

	if dataset == 'full':
			global full_data
			full_data.get_index_of_timestamp(user_input.timestamp)
	else:
		global holed_data
		holed_data.get_index_of_timestamp(user_input.timestamp)
	return render_template('index.html', data="abcd")

@app.route('/handle_input', methods=['POST'])
def handle_input():
	# Redirecting to different route: https://stackoverflow.com/questions/48148131/how-can-we-call-one-route-from-another-route-with-parameters-using-python-flask
    if request.method == "POST":
	    d = str(request.form['day'])
	    h = str(request.form['hour'])
	    da = str(request.form['dataset'])

    #print(f"Dataset is: {da}", flush=True)
    return redirect(url_for('home'), code=307)

# Set host to 0.0.0.0 so that it is accessible from 'outside the container'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)