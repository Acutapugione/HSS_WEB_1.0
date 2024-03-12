from .. import application as app
from flask import render_template, flash
from flask_login import login_required, current_user

@app.route("/", methods=["GET"])
@login_required
def home():
    # print(f"{current_user.email=}")
    return render_template("landing.html")


