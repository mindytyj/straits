from flask import Flask, render_template, request, jsonify, url_for
from config import database
from login import check_credentials
from flask import redirect


app = Flask(__name__)

# Routes
@app.route("/")
def login():
        return render_template("login.html")

@app.route("/login", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        user = check_credentials(username, password)

        if user:
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid email or password"

    return render_template('login.html', error=error)

@app.route("/dashboard")
def dashboard():
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("SELECT CourseID, CourseName, TrainingHours FROM Courses;")
    courses = dbquery.fetchall()
    dbquery.close()
    return render_template("dashboard.html", courses=courses)

@app.route("/courses")
def courses():
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("SELECT t1.CourseID, t1.CourseName from Courses t1 LEFT JOIN Training t2 on t1.CourseID = t2.CourseID LEFT JOIN Users t3 on t2.UserID = t3.UserID WHERE t2.UserID = 3;")
    data = dbquery.fetchall()
    dbquery.close()
    return render_template("courses.html", courses=data)

@app.route("/courses/<string:CourseID>/add", methods=['GET', 'POST'])
def addcourse(CourseID):
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("INSERT INTO Training (UserID, CourseID) VALUES (3, %s)", (CourseID,))
    dbquery.close()
    return redirect(url_for('courses'))

@app.route("/courses/<string:CourseID>/delete", methods=['GET', 'POST'])
def deletecourse(CourseID):
    dbquery = database.connection.cursor(dictionary=True)
    dbquery.execute("DELETE FROM Training WHERE UserID = 3 AND CourseID = %s", (CourseID,))
    dbquery.close()
    return redirect(url_for('courses'))

if __name__ == "__main__":
    app.run()
