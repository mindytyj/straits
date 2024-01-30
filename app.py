from flask import Flask

app = Flask(__name__)


@app.route("/")
def login():
    return "Login Page"

@app.route("/hr")
def hr():
    return "HR Page"

if __name__ == "__main__":
    app.run()
