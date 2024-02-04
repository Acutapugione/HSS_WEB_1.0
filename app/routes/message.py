from .. import application as app
# from app import application
from flask import render_template, request, flash
from .. forms import MessageForm
from db import Session, Department, Executor, Order
from sqlalchemy import select


@app.route("/message", methods=["GET", "POST"])
def message():
    form = MessageForm(request.form)
    
    if request.method == 'POST' and form.validate():
        target_sql = select(Department).where(Department.name == request.form.get("target"))
        executor_sql = select(Executor).where(Executor.name == request.form.get("executor"))
        
        with Session.begin() as session:
            order = Order(
                description=request.form.get("description"),
                phone=request.form.get("phone"),
                target = session.scalars(target_sql).first(),
                executor = session.scalars(executor_sql).first(),
            )
            session.add(order)
            flash(f'На ваш номер: {order.phone} відправлено повідомленням із підтвердженням заявки')

    return render_template("message.html", form=form)