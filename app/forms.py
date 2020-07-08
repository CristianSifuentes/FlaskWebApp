from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, ValidationError, BooleanField
from wtforms.fields.html5 import EmailField

from .models import User

def codi_validador(form, field):
    if field.data == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('codi is not forbbiden')
        

  
class LoginForm(Form):
    
    username = StringField('Username',[
        validators.length(min=4, max=50, message='Value betweeb 4 and 50')
        
    ])
    password = PasswordField('Password',[
        validators.Required(message='Password is requered')

    ])
    

class RegisterForm(Form):
    username = StringField('Username',[
        validators.length(min=4, max=50)
    ])
    email = EmailField('Email', [
        validators.length(min=5, max=100),
        validators.Required(message='Email is required.'),
        validators.Email(message='Email is not valid')
    ])
    password = PasswordField('Password',[
        validators.Required(message='Password is required.'),
        validators.EqualTo('confirm_password', message='The password is not equal')

    ])
    confirm_password = PasswordField('ConfirmPassword',[
        validators.Required(message='Conformation ,Password is required.')
    ])
    accept = BooleanField('', [
        validators.DataRequired()
    ])
    
    
    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('Username is used already')
        
    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('Email is used already')
        
        
    def validate(self):
        if not Form.validate(self):
              return False
          
        if len(self.password.data)< 3:
          self.password.errors.append('Password is short')
          return False
        
        return True