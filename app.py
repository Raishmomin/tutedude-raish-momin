from flask import Flask, jsonify, request, redirect, render_template
from pymongo import MongoClient
import json
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)


@app.route('/api')
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)



MONGO_URI = os.getenv('MONGO_URI')

# MongoDB Atlas setup
client = MongoClient(MONGO_URI)  
db = client['test']
collection = db['flask-tutorial']


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            collection.insert_one({'name': name, 'email': email})
            return redirect('/success')
        except Exception as e:
            error = str(e)
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)
