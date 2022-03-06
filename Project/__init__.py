# this is setting up the basics of a project
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# this secret if for forms
app.config['SECRET_KEY'] = 'somethingreallysecret'
# the userid password and server name all come from the docker compose file
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:yourpass143@mysql/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'

db = SQLAlchemy(app)
Migrate(app,db)

from Project.about.views import about_blueprint

app.register_blueprint(about_blueprint,url_prefix="/about")
