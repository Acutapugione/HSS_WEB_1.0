from wtforms import (Form, BooleanField, StringField, PasswordField,
                     validators, SubmitField, SelectField, TextAreaField, EmailField,)


class UserSignUpForm(Form):
    email = EmailField('Електронна пошта', [validators.Email(), validators.DataRequired()])
    pwd_first = PasswordField('Пароль', [validators.EqualTo('pwd_second'), validators.DataRequired()])
    pwd_second = PasswordField('Підтвердження пароля', [validators.EqualTo('pwd_second'), validators.DataRequired()])
    submit = SubmitField(
            'Зареєструватись',
            [validators.DataRequired()]
        )
    
class UserSignInForm(Form):
    email = EmailField('Електронна пошта', [validators.Email(), validators.DataRequired()])
    pwd = PasswordField('Пароль', [validators.DataRequired()])
    remember = BooleanField("Запам'ятати мене", default=False)
    submit = SubmitField('Авторизуватись',[validators.DataRequired()])

class UserProfileForm(Form):
    # email = EmailField('Електронна пошта', [validators.Email(), validators.DataRequired()])
    pwd_first = PasswordField('Пароль', [validators.EqualTo('pwd_second'), validators.DataRequired()])
    pwd_second = PasswordField('Підтвердження пароля', [validators.EqualTo('pwd_second'), validators.DataRequired()])
    submit = SubmitField(
            'Підтвтердити зміни',
            [validators.DataRequired()]
        )