from __future__ import print_function
from flask import Flask, render_template, url_for, request, redirect
import sys

app = Flask(__name__)


@app.route('/')
def main():
    print('Hello world', file=sys.stderr)
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if not username == "mathiasj" and password == 'selorenus12':
        return redirect('/') # TODO: hier weiter machen


def init_static_files():
    url_for('static')
    # url_for('static', filename='background.jpg')


if __name__ == '__main__':
    app.run(debug=True)
    init_static_files()
