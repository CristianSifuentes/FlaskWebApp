from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField

class LoginForm(Form):
    
    username = StringField('Username',[
        validators.length(min=4, max=50, message='Valor entre 4 y 50')
    ])
    password = PasswordField('Password',[
        validators.Required()
    ])
