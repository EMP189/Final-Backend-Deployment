from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_migrate import Migrate
from decouple import config

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lrqkpfekqguxgf:ffba5533044978c0a75243250e528dd4234b4cac0ad6c9fecd72996b490972ec@ec2-54-195-76-73.eu-west-1.compute.amazonaws.com:5432/d33lqip0ckbaf8'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


from flaskserver import routes