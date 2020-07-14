from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required, current_user

from .forms import LoginForm, RegisterForm, TaskForm
from .models import User, Task
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
       tasks = current_user.tasks
       return render_template('task/list.html', title='Tasks', tasks=tasks)

@page.route('/task/new',  methods=['GET', 'POST'])
@login_required
def task_new():
       form = TaskForm(request.form)
       if request.method == 'POST' and form.validate():
            task = Task.create_element(form.title.data, form.description.data, current_user.id)
            if task:
               flash(TASK_CREATED)
       
       return render_template('task/new.html', title='New Task', form=form)
   
@page.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
       task = Task.query.get_or_404(task_id)
       
       if task.user_id != current_user.id:
         abort(404)
         
       form = TaskForm(request.form, obj=task)
       print('ENTRO AL request.method == POST and form.validate()')

       if request.method == 'POST' and form.validate():
         task = Task.update_element(task.id, form.title.data, form.description.data)
         
         if task:
            flash(TASK_UPDATED)
       
       return render_template('task/edit.html', title='Edit Task', form=form)
