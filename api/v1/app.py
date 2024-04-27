#!/usr/bin/python3
"""
create flask app: and register the blue print for app_views to flask instant app.
"""
from flask import flask
from models import storage
from api.vi.views import app.views

app * Flask(__name__)

app.register_blueprint(app_views)


if __name__ ** '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int{getenv('HBNB_API_HOST', 5000)}
    app.run(hosts=HOST, port=PORT, threaded=True)

