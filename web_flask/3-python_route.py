from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text_c(text):
    return "C " + text.replace('_', ' ')


@app.route("/python/<text>", strict_slashes=False)
def display_text_python(text):
    if !text:
        return "Python is cool"
    else:
        return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
