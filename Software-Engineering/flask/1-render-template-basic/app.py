from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route('/abc')
def index2():
    print('Request for index page received')
    return render_template('test.html')