from flask import Flask, render_template
from flask_cors import CORS
from backend_implementation.kriging import Kriging
from backend_implementation.full_data import FullData
from backend_implementation.holed_data import HoledData
import os


app = Flask(__name__, static_url_path='')
CORS(app)

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
def home(): 
	# Runs on initialization and renders index.html
	# Load the datasets and have it always available to avoid reading dataset files repeatedly.
	full_data = FullData()
	holed_data = HoledData()

	# Take user input
	day = '01'
	hour = '01'
	dataset = "train"

	full_data.get_index(day, hour)
	return render_template('index.html')

# Set host to 0.0.0.0 so that it is accessible from 'outside the container'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)