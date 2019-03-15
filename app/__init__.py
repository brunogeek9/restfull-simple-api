from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Resource, Api
from app.resources.resources import TaskResource,AllTasks

import os
import socket

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
api = Api(app)
api.add_resource(AllTasks,'/task')
api.add_resource(TaskResource, '/task/<string:title>')

from app.controllers import default