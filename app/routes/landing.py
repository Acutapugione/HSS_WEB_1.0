from .. import application as app
from flask import render_template, flash

@app.route("/landing", methods=["GET"])
def landing():
    return render_template("landing.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")
