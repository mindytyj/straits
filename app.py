from flask import Flask, render_template, request, jsonify, url_for
from config import database
from login import check_credentials
from flask import redirect
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

def login_page():
    return render_template("login.html")

@app.route("/submit. methods=['POST']")
def submit():
    username = request.form['email']
    password = request.form['password']

    user = check_credentials(username, password)

    if user:
        return redirect(url_for('index'))
    else:
        return jsonify({"success": False})

@app.route("/hr")
def hr():
    return "HR Page"

if __name__ == "__main__":
    app.run()
