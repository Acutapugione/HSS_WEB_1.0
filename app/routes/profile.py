from .. import application as app
# from app import application
from flask import redirect, render_template, request, flash, url_for
from .. forms import MessageForm, UserProfileForm
from db import Session, Department, Executor, Appeal, User
from sqlalchemy import select
from flask_login import current_user, login_required
from . import AUTH_CONTEXT

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UserProfileForm(request.form)
    if request.method == "POST":
        if not form.validate():
            print(f"{form.errors=}")
            return redirect(url_for("home"))
        user_sql = select(User).where(User.email == current_user.email)
        with Session.begin() as session:
            user = session.scalars(user_sql).first()
            user.set_password(form.pwd_first.data)
            session.add(user)
            
            return redirect(url_for("logout"))
    context = {
        'form' :form,
    }
    context.update(AUTH_CONTEXT)
    return render_template("crud_form.html", **context)
