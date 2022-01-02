from enum import unique
from re import template
from flask import Flask
from flask import url_for
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect
import requests
import json
import os
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.sql import text


application = Flask(__name__)
#applicationlication.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/realestatelogin.user'
#db = SQLAlchemy(applicationlication)
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, passw):
        self.username = username
        self.email = email
        self.password = passw

    def __repr__(self):
        return '<User %r>' % self.username
'''

#admin = User('admin', 'admin@example.com', "examplePassword")

#db.session.add(admin)

rawData = open('raw_data.json')

finalData = open('static/final_data.txt', 'w',)

data = json.load(rawData)
finalData.write("\n")
for i in data["meals"]:
    try: 
        finalData.write("'" + i["strMeal"]+ "'" + ","+"\n")
    except Exception as e:
        continue


rawData.close()
finalData.close()

@application.route("/")
def homePage():
    return render_template('index.html')



@application.route('/search', methods=['POST', 'GET'])
def searchFood(term = None):
    searchtTerm = request.args.get('term')
    print(searchtTerm)
    url = 'http://www.themealdb.com/api/json/v1/1/search.php?s=' + searchtTerm
    foodData = requests.get(url).json()
    print(foodData)
    if(foodData['meals'] == None):
        return 'error bad user input'
    return foodData









    
if __name__ == '__main__':
    application.run(debug=True)