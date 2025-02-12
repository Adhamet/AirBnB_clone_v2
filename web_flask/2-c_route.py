#!/usr/bin/python3
"""Starts flask web application with specific requirements"""
from flask import Flask, escape

app = Flask(__name__)


# Define Hello-HBNB-Route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints Hello HBNB"""
    return 'Hello HBNB!'


# Define HBNB-Route
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return 'HBNB'


# Define C-Route
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays C followed by customtext"""
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    """run flask web-app"""
    app.run(host='0.0.0.0', port=5000)
