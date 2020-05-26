import contexts,os
dir=os.path.abspath(os.path.dirname(__file__))
from instance.config import *
#flask
from flask import Flask,render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('../instance/config.py')
mail = Mail(app)

#celery
from celery import Celery
from config import *
celery = Celery(app.import_name ,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_async_email(to, subject, template, **kwargs):
    msg = Message(MAIL_SUBJECT_PREFIX + ' ' + subject,
                  sender=MAIL_SENDER, recipients=[to])
    with app.app_context():
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)
    print("Mail Sent")
