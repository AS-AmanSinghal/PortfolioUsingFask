import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def Index1():
    return render_template('index.html')


@app.route('/<string:fileName>')
def Index(fileName):
    return render_template(fileName)


def writeInFile(data):
    with open('database.txt', mode='w+') as myFile:
        myFile.write(f"{data}")


def writeInCSV(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as myFile:
        csvWriter = csv.writer(myFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvWriter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            writeInFile(data)
            writeInCSV(data)
            print(data)
        except:
            return "Didn't save into Database"
    else:
        return 'Something Wents Wrong'
    return render_template('thankyou.html')
