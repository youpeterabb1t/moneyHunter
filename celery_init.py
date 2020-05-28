from celery import Celery
#flask
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment

import atexit

from api.instance import config
"""
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
"""
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
app = Flask(__name__, instance_relative_config=True)  # modified 20191108
app.config.from_object('api.config')
app.config.from_object('api.instance.config')
app.config.from_pyfile('config.py')
#config[config_name].init_app(app)
bootstrap.init_app(app)
moment.init_app(app)
#login_manager.init_app(app)
mail.init_app(app)
celery = Celery(app.import_name ,broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

#blueprint part
from webapp import main as main_blueprint
app.register_blueprint(main_blueprint.main)
from api.agent import ssimulate
ssimulate.delay()