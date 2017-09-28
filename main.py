from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


def init_static_files():
    url_for('static', filename='style.css')
    url_for('static', filename='background.jpg')


if __name__ == '__main__':
    app.run(debug=True)
    init_static_files()
