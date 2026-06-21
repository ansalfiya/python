from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy Credentials
USERNAME = "admin"
PASSWORD = "admin@123"

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))
    else:
        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)