#!/usr/bin/python3
"""importing Flask"""
from flask import Flask
app = Flask(__name__)
@app.route("/", strict_slashes=False)
"""Difining hello fun"""
def hello_hbnb:
    """display Hello HBNB"""
    return("Hello HBNB!")
if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000)
