from flask import Blueprint
from flask import render_template

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_notfound(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='index')