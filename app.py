from flask import Flask
from flask_restplus import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from apis.user.resources import User
from connectors.db_configurations.postgres_db import POSTGRES_CONFIGURATIONS

__all__ = ['app', 'api', ]

app = Flask(__name__)
api = Api(app)

# routes
api.add_resource(User, '/user')

# db initialization
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'.format(
                                            **POSTGRES_CONFIGURATIONS
                                        )
ps_db = SQLAlchemy(app)
migrate = Migrate(app, ps_db)
from repository.models import *  # this needs to be imported though it is not explicitly used
