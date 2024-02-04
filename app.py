from flask import Flask, render_template, request
from config import database

from login import login

app = Flask(__name__)

dbquery = database.connection.cursor()
dbquery.execute("")
dbquery.close()
database.connection.close()

# Routes
@app.route("/")
def index():
    return render_template("dashboard.html")

def login():
    # dbquery = connection.cursor()
    # dbquery.execute("SQL QUERY HERE")
    # dbquery.close()
    # connection.close()
    return render_template("login.html")

@app.route("/submit. methods=['POST']")
def submit():
    username = request.form['username']
    password = request.form['password']
    return login(username, password)

@app.route("/hr")
def hr():
    return "HR Page"

if __name__ == "__main__":
    app.run()
