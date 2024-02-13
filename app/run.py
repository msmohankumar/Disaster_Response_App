# run.py
from flask import Flask, render_template

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('master.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    # You can pass data to this page if needed
    return render_template('go.html'), 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)
