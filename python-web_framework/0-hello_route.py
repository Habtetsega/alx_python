#!/usr/bin/python3
"""
flask: A popular Python web framework for building web applications easily.

This module provides tools and libraries for handling HTTP requests, rendering templates, managing sessions, and more.

Usage:
    import flask

    # Example usage
    app = flask.Flask(__name__)
    ...

"""
from flask import Flask
app = Flask(__name__)
@app.route("/", strict_slashes=False)
"""Difining hello fun"""
def hello_hbnb:
    """display Hello HBNB"""
    return("Hello HBNB!")
if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000)
