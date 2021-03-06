from flask_script import Manager, Shell, Server
from celery_init import app,celery

manager = Manager(app)


def make_shell_context():
	return dict(app=app, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

if __name__ == '__main__':
	manager.run()


