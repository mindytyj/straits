from flask import Flask, render_template, request

from login import login

# import os
# from dotenv import load_dotenv
# import mysql.connector
#
# load_dotenv(".env")
#
app = Flask(__name__)
#
# # Database Configuration
# connection = mysql.connector.connect(
#     user=os.getenv('DB_USER'),
#     password=os.getenv('DB_PASSWORD'),
#     host=os.getenv('DB_HOST'),
#     port=os.getenv('DB_PORT'),
#     database=os.getenv('DB_NAME')
# )

# Routes

@app.route("/")
def index():
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
