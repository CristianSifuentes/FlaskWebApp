from flask_mail import Message
from flask import current_app, render_template
from . import mail

def welcome_mail(user):
    message = Message('Welcome', 
                      sender=current_app.config['MAIL_USERNAME'],
                      recipients=[user.email])
    message.html = render_template('email/welcome.html', user=user)
    
    mail.send(message)