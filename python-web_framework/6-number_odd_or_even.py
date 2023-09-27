from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    new_text = text.replace("_", " ")
    return ("C {}".format(next_text))

@app.route('/python/<text>', defaults={"text":"is cool"}, strict_slashes=False)
def pytext(text):
    new_text = text.replace("_", " ")
    return ("Python {}".format(new_text))
@app.route('/converters/')
@app.route('/number/<int:n>')
def is_int(n):
    if isinstance(n, int):
        return ("{} is a number".format(n))

@app.route('/converters/')
@app.route('/number_template/<n><int:n>')
def is_int(n):
    if isinstance(n, int):
        return render_template("templates/5-number.html", num=n)

@app.route('/converters/')
@app.route('/number_template/<n><int:n>')
def is_int(n):
    if isinstance(n, int):
        return render_template("templates/6-number_odd_or_even.html", num=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
