from flask import Flask, render_template, request
from config import database
from login import login

app = Flask(__name__)

# Routes
@app.route("/")
def index():
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("SELECT CourseID, CourseName, TrainingHours FROM Courses;")
    courses = dbquery.fetchall()
    dbquery.close()
    return render_template("dashboard.html", courses=courses)

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

    dbquery = database.connection.cursor()
    dbquery.execute(f"SELECT Username, Password FROM Users WHERE Username = `{username}` AND Password = `{password}`);")
    dbquery.close()
    database.connection.close()

    return

@app.route("/hr")
def hr():
    return "HR Page"

if __name__ == "__main__":
    app.run()
