import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcome!'

@app.route('howareyou')
def hello():
    return 'I am good. How are you?'


if __name__ == '__main__':
    app.route(host='0.0.0.0', port=8080)
