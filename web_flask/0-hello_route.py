from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False) # Hace referencia a la raíz de la pag
def home():
    return "Hello HBNB!" # Lo que retornará en la pag

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
