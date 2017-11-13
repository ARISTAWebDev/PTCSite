""" manage.py 

This is a command line tool to manage the flask app

The author is aware of the newer integrated 'flask' command, but the support for the factory generation model of the flask app

"""

from flask_script import Manager

from app.application import get_config, create_app

config = 'app.config.Testing'

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)

@manager.command
def hello():
    print 'bye'

if __name__ == "__main__":
    manager.run()
