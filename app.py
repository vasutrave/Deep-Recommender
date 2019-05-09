
import os
from flask import Flask, render_template
from routes import *
import pandas as pd 

metadata = pd.read_csv('database_metadata.csv')
ratings = pd.read_csv('ratings_small.csv')
app = Flask(__name__)
app._static_folder = os.path.join(os.getcwd(),"static")
app.config['SECRET_KEY'] = '59d3ca27e6701d3fd06eb960ca5866a5'

@app.route('/')
def default():
	return route_login()

@app.route('/login', methods=["GET", "POST"])
def login():
	return route_login()

@app.route('/home')
def home():
	return route_home()

@app.route('/details/<movieId>', methods=["GET","POST"])
def details(movieId):
	return route_details(movieId)

@app.route('/update', methods=["GET","POST"])
def update_rating():
	return route_update_rating()


@app.route('/logout')
def logout():
    return route_logout()

if __name__ == '__main__':
   app.run(host = '0.0.0.0',port = 5000,debug = True)