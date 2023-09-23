#!/usr/bin/python3
"""Starts flask web application with specific requirements"""
from flask import Flask, escape, render_template

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
@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c_text(text='is_cool'):
    """displays C followed by customtext"""
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)


# Define Python-Rotue
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    """displays Python followed by custom text"""
    text = escape(text).replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
     """displays n if number"""
     return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display HTML page if n is an intger"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """run flask web-app"""
    app.run(host='0.0.0.0', port=5000)
