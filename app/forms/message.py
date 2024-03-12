from wtforms import (Form, BooleanField, StringField, PasswordField,
                     validators, SubmitField, SelectField, TextAreaField, EmailField)
from db import Session, Department, Executor, Order
from sqlalchemy import select

with Session.begin() as session:
    class MessageForm(Form):
        phone = StringField(
            'Phone', [
                validators.Length(min=13, max=13)], default="+380"
        )
        target = SelectField(
            'Місце проведення',
            choices=[str(x) for x in session.scalars(select(Department)).all()]
        )
        executor = SelectField(
            'Виконавець',
            choices=[str(x) for x in session.scalars(select(Executor)).all()]
        )
        submit = SubmitField(
            'Оформити заявку',
            [validators.DataRequired()]
        )
        description = TextAreaField(
            'Опис заявки',
            [validators.Length(min=10, max=255)]
        )

