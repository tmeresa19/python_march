from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "password1234"







# At the very end don't forget to place the "run" command
if __name__ == "__main__":
    app.run(debug = True, port=5001 )
