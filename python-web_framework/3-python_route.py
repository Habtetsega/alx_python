"""
Import Flask From flask

"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
"""
display 'Hello HBNB!'
"""
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
"""
display 'HBNB'
"""
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
"""
display 'C <text>'
"""
def ctext(text):
    new_text = text.replace("_", " ")
    return ("C {}".format(next_text))

@app.route('/python/<text>', defaults={"text":"is cool"}, strict_slashes=False)
"""
display 'Python <text>'
"""
def pytext(text="is cool"):
    new_text = text.replace("_", " ")
    return ("Python {}".format(new_text))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
