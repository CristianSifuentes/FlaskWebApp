from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from .forms import LoginForm, RegisterForm
from .models import User
from .consts import *
from . import login_manager

page = Blueprint('page', __name__)



@login_manager.user_loader
def load_user(id):
    return User.get_by_id(id)

@page.app_errorhandler(404)
def page_notfound(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='index')

@page.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT)
    return redirect(url_for('.login'))
    
@page.route('/login', methods=['GET', 'POST'])
def login():
    
   if current_user.is_authenticated:
       return redirect(url_for('.task')) 
   
   form = LoginForm(request.form)
   
   if request.method == 'POST' and form.validate():
       
       user = User.get_by_username(form.username.data)
       if user and user.check_password(form.password.data):
           login_user(user)
           flash(LOGIN_SUCCESS)
           print('bien')
           return redirect(url_for('.task'))
       else:
           flash(ERROR_USER_PASSWORD, 'error')
           print('no bien')


   return render_template('auth/login.html', title='login', form = form)

@page.route('/register',  methods=['GET', 'POST'])
def register():
     
       if current_user.is_authenticated:
            return redirect(url_for('.task'))  
   
       form = RegisterForm(request.form)
       if(request.method == 'POST'):
           if form.validate():
            user = User.create_element(form.username.data, form.password.data, form.email.data)            
            flash(USER_CREATED)
            login_user(user)
            return redirect(url_for('.task'))  

       return render_template('auth/register.html', title='Register', form=form)

@page.route('/task')
@login_required
def task():
       return render_template('task/list.html', title='Tasks')