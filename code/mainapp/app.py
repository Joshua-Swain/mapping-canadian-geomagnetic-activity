
from flask_cors import CORS
from flask import Flask, render_template

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
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8001)