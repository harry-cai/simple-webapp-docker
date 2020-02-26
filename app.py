import os
import random
import socket

from flask import Flask
from flask import render_template

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

app = Flask(__name__)
color = os.environ.get('APP_COLOR') or random.choice(
    ["red", "green", "blue", "blue2", "darkblue", "pink"])


@app.route('/')
def main():
    return 'Welcome!'


@app.route('/howareyou')
def hello():
    return 'I am good. How are you?'


@app.route("/color")
def default_color():
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])


@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
