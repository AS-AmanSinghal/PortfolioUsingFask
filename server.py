from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Index1():
    return render_template('index.html')


@app.route('/<string:fileName>')
def Index(fileName):
    return render_template(fileName)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'A form Submitted Successfully...'
