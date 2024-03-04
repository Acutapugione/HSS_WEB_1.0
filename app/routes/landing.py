from .. import application as app
from flask import render_template

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")