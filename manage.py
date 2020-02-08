from flask_migrate import MigrateCommand
from flask_script import Manager, Server, Shell
from app import app


manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('shell', Shell)
manager.add_command('ps_db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
