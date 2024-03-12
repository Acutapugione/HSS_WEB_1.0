from flask import Flask
from dotenv import load_dotenv
from os import getenv
import flask_login

load_dotenv()

application = Flask(__name__, template_folder="../templates", static_folder="../static")
application.secret_key = getenv("SECRET_KEY")

login_manager = flask_login.LoginManager()
login_manager.init_app(application)

from app import routes