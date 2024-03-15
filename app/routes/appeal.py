from .. import application as app
# from app import application
from flask import redirect, render_template, request, flash, url_for
from ..forms import MessageForm
from db import Session, Department, Executor, Appeal, User, Status
from sqlalchemy import select
from flask_login import current_user, login_required
from . import AUTH_CONTEXT, API_WORKER

@login_required
def update_appeal(session, form, id):
    target_sql = select(Department).where(Department.name == form.target.data)
    executor_sql = select(Executor).where(Executor.name == form.executor.data)
    order_sql = select(Appeal).where(Appeal.id == id)
    order = session.scalars(order_sql).first()
    order.description=form.description.data
    order.phone=form.phone.data
    order.executor = session.scalars(executor_sql).first()
    order.target = session.scalars(target_sql).first()
    session.add(order)
    return True

@login_required
def save_appeal(session, form):
    target_sql = select(Department).where(Department.name == form.target.data)
    executor_sql = select(Executor).where(Executor.name == form.executor.data)
    user_sql = select(User).where(User.email == current_user.email)
    order = Appeal(
        user=session.scalars(user_sql).first(),
        description=form.description.data,
        phone=form.phone.data,
        target = session.scalars(target_sql).first(),
        executor = session.scalars(executor_sql).first(),
        status = Status(title="Pending"),
    )
    session.add(order)
    return True
    
@app.route("/create_appeal", methods=["GET", "POST"])
@login_required
def create_appeal():
    context = {}
    context.update(AUTH_CONTEXT)
    form = MessageForm(request.form)
    
    if request.method == 'POST' and form.validate():
        with Session.begin() as session:
            save_appeal(session, form)
            API_WORKER.post_message({
                "text": form.description.data,
                "phone_number": form.phone.data,
            })
            flash(f'На ваш номер: {form.phone.data} відправлено повідомленням із підтвердженням заявки')
            return redirect(url_for("appeals"))
    context.update({'form': form})
 
    return render_template("crud_form.html", **context)

@app.route("/appeals/<int:id>", methods=["GET", "POST"])
@login_required
def appeal(id):
    context = {}
    context.update(AUTH_CONTEXT)
    form = MessageForm(request.form)

    if request.method == 'POST':
        if not form.validate():
            return redirect(url_for("appeals"))
        with Session.begin() as session:
            update_appeal(session, form, id)
            API_WORKER.post_message({
                "text": form.description.data,
                "phone_number": form.phone.data,
            })
            flash(f'На ваш номер: {form.phone.data} відправлено повідомленням із підтвердженням заявки')
            return redirect(url_for("appeals"))
    appeal_sql = select(Appeal).where(Appeal.id == id)
    with Session.begin() as session:
        appeal_item = session.scalars(appeal_sql).first()
        if not appeal_item:
            flash("Нажаль такого елемента не знайдено", category="error")
            print(f"Нажаль {id} елемента не знайдено")
            redirect(request.args.get('next') or url_for("appeals"))
        form = MessageForm(obj=appeal_item)
        context.update({'form': form})
        return render_template("crud_form.html", **context)
    

@app.route("/appeals", methods=["GET"])
@login_required
def appeals():
    context = {}
    context.update(AUTH_CONTEXT)
    with Session.begin() as session:
        user =  session.scalars(select(User).where(User.email == current_user.email)).first()
        print(f"{user=}")
        if user:
            orders = session.scalars(select(Appeal).where(Appeal.user_id == user.id)).all()
            context["items"] = orders
        return render_template("index.html", **context)