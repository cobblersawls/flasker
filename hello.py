from pkgutil import ImpImporter
from flask import Flask, render_template

# Create a Flask instance

app = Flask(__name__)


# Possibilities using jinja2 methods
# FILTERS safe (allows html to be parsed to the app), capitalize, lower, upper, title, trim, striptags (strips html tags)

# Create a route decorator

@app.route('/')

# def index():
#     return "<h1>Hello world!</h1>"

def index():
    first_name = 'Tom'
    stuff = 'This is <strong> bold </strong> text'
    motorbike_list = ['ducati', 'benelli', 'vespa', 'bsa']
    return render_template("index.html", 
    first_name=first_name,
    stuff=stuff,
    motorbike_list = motorbike_list)

# localhost:5000/user/John
@app.route('/user/<name>') 

def user(name):
    # return "<h1>Hello {}</h1>".format(name)
    return render_template("users.html", user_name=name)

# Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

# internal server error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500