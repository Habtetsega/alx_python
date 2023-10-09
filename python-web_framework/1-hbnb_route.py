"""
Flask Web Application

This module contains a simple Flask web application with two routes: "/" and "/hbnb".

Routes:
    /: Displays "Hello HBNB!"
    /hbnb: Displays "HBNB"

Usage:
    $ python app.py

    The web application will start and listen on 0.0.0.0:5000.
    Visit http://localhost:5000/ to see the message "Hello HBNB!".
    Visit http://localhost:5000/hbnb to see the message "HBNB".

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

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB".

    Returns:
        str: The message "HBNB".
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
