from . import ANONYMOUS_CONTEXT
from .. import application as app
from flask import render_template, flash

@app.route("/", methods=["GET"])
def landing():
    context = {}
    # print(f"{current_user.email=}")
    context.update(ANONYMOUS_CONTEXT)
    return render_template("landing.html", **context)


@app.route("/about", methods=["GET"])
def about():
    context = {}
    # print(f"{current_user.email=}")
    context.update(ANONYMOUS_CONTEXT)
    return render_template("about.html", **context)
