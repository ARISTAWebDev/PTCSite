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
def hell():
    print 'hell'

@manager.command
def create_db():
    print 'Creating database...'
    print 'Importing necessary libraries...'
    
    from migrate.versioning import api
    from app.extensions import db
    import os.path

    db.create_all()
    print 'Success: Database created'
    
    print 'Initializing migrations...'
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

    print 'Database created and migrations setup...'

if __name__ == "__main__":
    manager.run()
