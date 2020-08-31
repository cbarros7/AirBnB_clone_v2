from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route("/")
def route():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def display_text_c(text):
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
