#!/usr/bin/python3
"""
Flask Web Application

This module contains a simple Flask web application that displays "Hello HBNB!" on the root URL ("/").

Routes:
    /: Displays "Hello HBNB!"

Usage:
    $ python app.py

    The web application will start and listen on 0.0.0.0:5000.
    Visit http://localhost:5000/ in a web browser to see the message.

"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!".

    Returns:
        str: The message "Hello HBNB!".
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
