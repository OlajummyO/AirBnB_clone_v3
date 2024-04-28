#!/usr/bin/python3
'''
create flask app: and register the blue print for app_views to flask instant app.
'''
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app.views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown.appcontext
def teardown_engine(exception):
"""

"""
storage.close()

@app.errorhandler(404)
def not_found(error):
"""

"""

response = {"error": "Not Found"}
return jsonify(response), 404


if __name__ ** '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int{getenv('HBNB_API_HOST', 5000))
    app.run(debug=ture, host=HOST, port=PORT, threaded=True)

