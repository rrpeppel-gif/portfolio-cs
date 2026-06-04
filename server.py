from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/over-mij")
def over_mij():
    return render_template("over-mij.html")

@app.route("/projecten")
def projecten():
    return render_template("projecten.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/punishing-home")
def punishing():
    return render_template("punishing-home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)