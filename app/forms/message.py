from wtforms import (Form, BooleanField, StringField, PasswordField,
                     validators, SubmitField, SelectField, TextAreaField, EmailField)
from db import Session, Department, Executor, Appeal
from sqlalchemy import select


with Session.begin() as session:
    class MessageForm(Form):
        phone = StringField(
            'Phone', 
            validators=[validators.Length(min=13, max=13, message="Номер телефону повинен бути не менше %(min)d та не більше %(max)d символів")], 
            default="+380",
            render_kw={"class": "form-control"},

        )
        target = SelectField(
            'Місце проведення',
            choices=[str(x) for x in session.scalars(select(Department)).all()],
            render_kw={"class": "form-select"},
        )
        executor = SelectField(
            'Виконавець',
            choices=[str(x) for x in session.scalars(select(Executor)).all()],
            render_kw={"class": "form-select"},

        )
        description = TextAreaField(
            'Опис заявки',
            [validators.Length(min=10, max=255)],
            render_kw={"class": "form-control"},
            )
        submit = SubmitField(
            'Оформити заявку',
            [validators.DataRequired()],
            render_kw={"class":"btn btn-outline-primary"}
        )
        

