from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    h='hola mundo'
    return h


if __name__ == '__main__':
    app.run()
