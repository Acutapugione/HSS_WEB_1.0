from .. import application as app, login_manager
from .. forms import UserSignUpForm, UserSignInForm
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user, current_user, login_required
from db import Session, User
from sqlalchemy import select
from . import ANONYMOUS_CONTEXT, AUTH_CONTEXT


@login_manager.user_loader
def user_loader(user_id):
    with Session.begin() as session:
        user = session.scalars(select(User).where(User.email == user_id)).first()  
        if user:
            return User(
                email=user.email, 
                authenticated=user.authenticated,
            )


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    context = {
    }
    context.update(ANONYMOUS_CONTEXT)
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = UserSignInForm(request.form)
    if request.method == "POST":
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        remember = request.form.get("remember", False)
        with Session.begin() as session:
            user = session.scalars(select(User).where(User.email==email)).first()
            if not user:
                flash('Будь ласка, перевірте свою електронну пошту та спробуйте ще раз.', category="error")
                return redirect(url_for("sign_up"))

            if not user.check_password(pwd):
                flash('Будь ласка, перевірте свій пароль і спробуйте ще раз.', category="error")
                return redirect(url_for("sign_up"))
            user.authenticated = True 
            login_user(user, remember=remember)
            return redirect(url_for("home"))

    context['form'] = form
    return render_template("sign_in.html",  **context)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    context = {}
    context.update(ANONYMOUS_CONTEXT)
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = UserSignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        with Session.begin() as session:
            user_exist = session.scalars(select(User).where(User.email == form.email.data)).first()
            if user_exist:
                flash("Нажаль користувач із такою електронною поштою вже зареєстрований, спробуйте ввійти або використайте іншу електронну пошту", 
                      category="error")
                return redirect(url_for("sign_up"))
            new_user = User(
                email = form.email.data, 
                authenticated = True,
            )
            new_user.set_password(form.pwd_first.data)
            session.add(new_user)
            login_user(new_user)
            return redirect(url_for("home"))

    context['form'] = form
    return render_template("sign_up.html", **context)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

