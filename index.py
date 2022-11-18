from flask import  Flask,request , jsonify

import util

app = Flask(__name__)



@app.route('/define')
def hello():
	return "For predicting the house price."


@app.route('/predictPrice')
def get_location():
	res = jsonify({
		'locations': util.get_location_names()
		})
	res.headers.add('Access-Control-Allow-Orgin','*')

	return res


if __name__ == "__main__":
	print("Server Running........")
	app.run()