
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/destination/<destination_id>')
def destination_details(destination_id):
    return render_template('destination_details.html', destination_id=destination_id)

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
