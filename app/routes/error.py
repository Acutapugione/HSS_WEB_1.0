from .. import application as app
from flask import redirect


@app.errorhandler(404)
def page_not_found(error):
    return redirect("/")