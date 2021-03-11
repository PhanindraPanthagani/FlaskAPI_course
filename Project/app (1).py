from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
#SQLALCHEMY_DATABASE_URI is the URL at which we can access 
#the database

#SQL alchemy is just a connection to the database from the
#Flask Front end 

db = SQLAlchemy(app)  #database object

#We need a data model to use the database, we will create 
#this in models.py

from routes import *


if __name__ == '__main__':
    app.run(debug = True)