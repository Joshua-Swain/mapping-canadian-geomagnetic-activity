from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os
from backend_implementation.kriging import Kriging
from backend_implementation.full_data import FullData
from backend_implementation.holed_data import HoledData
from backend_implementation.user_input import UserInput

# Create global variables to store the contents of the dataset
full_data = None
holed_data = None

app = Flask(__name__, static_url_path='')
CORS(app)


# Load the datasets before the very first user request and have it available during the entire lifespan of the application.
# Hence, time taken for file I/O is reduced as the csv files (i.e datasets) are only read once and not for every user request.
@app.before_first_request
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

@app.route('/')
def go_home():
	return redirect(url_for('home'))

@app.route('/magnetic-field-canada', methods=['POST', 'GET'])
def home(day='01', hour='01', dataset='full'): 
	# Handle the input provided by the user on the browser i.e DD-HH & dataset type.
	# If no input is provided (i.e GET request), use 01-01 & 'full' dataset as default
	if request.method == 'POST':
		form_values = request.form.to_dict()
		day = form_values['day']
		hour = form_values['hour']
		dataset = form_values['dataset']
		print(f"POST request: {day, hour, dataset}", flush=True)
	else:
		print(f"GET request: {day, hour, dataset}", flush=True)		

	# Store the user input as an object
	user_input = UserInput(day, hour, dataset)

	# Find the index of the row corresponding to the DD-HH timestamp provided by the user 
	# in the specified dataset. If not found, use the default values 01-01 & 'full' dataset.
	# Use the index and dataset to Krige (interpolate) and determine the magnetic field
	# reading for the given timestamp.
	if dataset == 'full':
			global full_data
			index = full_data.get_index_of_timestamp(user_input.timestamp)
			kriging = Kriging(index, full_data)
	else:
		global holed_data
		index = holed_data.get_index_of_timestamp(user_input.timestamp)
		kriging = Kriging(index, holed_data)

	json_data = kriging.kriging_output_json
	return render_template('index.html', data=json_data)

@app.route('/handle_input', methods=['POST'])
def handle_input():
    if request.method == "POST":
    	return redirect(url_for('home'), code=307)
    else:
    	return redirect(url_for('home'))

# Set host to 0.0.0.0 so that it is accessible from 'outside the container'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8001)))