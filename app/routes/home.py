from .. import application as app
from flask import render_template, flash
from flask_login import login_required, current_user
from . import AUTH_CONTEXT


@app.route("/home", methods=["GET"])
@login_required
def home():
    context = {}
    # print(f"{current_user.email=}")
    context.update(AUTH_CONTEXT)
    return render_template("index.html", **context)


