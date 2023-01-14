from flask import Flask, render_template

app = Flask(__name__)

companies = [
    {
        'Name':'Microsoft',
        'Country': 'USA',
        'Ticker': 'MSFT'
    },
    {
        'Name':'Facebook',
        'Country': 'USA',
        'Ticker':'FB'
    }
]

# Template Engine used by Flask - Jinja2

@app.route('/')
def basic():
    return render_template('index.html',companies=companies)  #title not provided, Else wala should print

@app.route('/about')
def about():
    return render_template('about.html',title = 'yesdeepakmittal')  # title provided, If wala should print

# if __name__ == '__main__':
#     app.run()