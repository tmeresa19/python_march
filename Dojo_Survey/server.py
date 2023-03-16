# Steps to create a flask app
# 1. pip install pipenv (follow the screenshot image)
# 2.
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "password1234"





@app.route('/todos', methods=['GET'])
def get_todos():
     return render_template("home.html", list_of_todos=list_of_todos)

