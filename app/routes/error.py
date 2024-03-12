from .. import application as app, login_manager
from flask import redirect, url_for


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("home"))

@app.errorhandler(401)
def page_not_found(error):
    return redirect(url_for("sign_in"))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("sign_in"))