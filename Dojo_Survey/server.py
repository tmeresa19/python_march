# Steps to create a flask app
# 1. pip install pipenv (follow the screenshot image)
# 2.
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "password1234"






@app.route('/todos', methods=['GET'])
def get_todos():
    return render_template("home.html", list_of_todos=list_of_todos)


"""
Method: GET
Getting all of a particular list
Function: get_all_todos()
          get_todos()
Url: '/todos'

Method: GET
Getting one item of a particular list
Function: get_todo_by_id( id )
          get_todo( id )
Url: '/todo/<int:todo_id>'
     '/todo/<int:id>'

Method: GET
Displaying a form that will eventually refer to a list
Function: display_todo_form()
Url: '/todo/form'

Method: POST
Create a new item of a particular list
Function: create_todo()
          add_todo()
Url: '/todo/new'
     '/todo/add'

Method: POST/PUT
Update an existing item of a particular list
Function: update_todo( id )
          edit_todo( id )
Url: '/todo/update'
     '/todo/edit'

Method: POST/DELETE
Remove an existing item from a particular list
Function: delete_todo( id )
          remove_todo( id )
Url: '/todo/delete'
     '/todo/remove'
"""
