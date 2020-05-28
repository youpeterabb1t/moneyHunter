import os
import api.e_mail.contexts
#config load
import api.config
from api.instance.config import *
#celery
from celery_init import celery,app,mail
from flask import Flask,render_template
from flask_mail import Mail, Message


@celery.task
def send_async_email(to, subject, template, **kwargs):
    msg = Message(MAIL_SUBJECT_PREFIX + ' ' + subject,
                  sender=MAIL_SENDER, recipients=[to])
    with app.app_context():
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)
    print("Mail Sent")
