#!/usr/bin/python3
"""Starts flask web application with specific requirements"""
from flask import Flask

app = Flask(__name__)


# Define Route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints Hello HBNB"""
    return 'Hello HBNB!'


# Define Route
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    """run flask web-app"""
    app.run(host='0.0.0.0', port=5000)
