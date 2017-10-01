from __future__ import print_function
from flask import Flask, render_template, url_for, request, session  # TODO: start implementing the session specific stuff
import sys

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(request.form, file=sys.stderr)
    if username == "mj" and password == 'secretpassword':  # TODO: replace passwords with a user manager and JSON loader
        return "ok"
    return "error"


@app.route('/dashboard')
def dashboard():
    return "Dashboard"


def init_static_files():
    url_for('static')
    # url_for('static', filename='background.jpg')


if __name__ == '__main__':
    app.run(debug=True)
    init_static_files()
