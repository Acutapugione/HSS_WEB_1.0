from flask import Flask


application = Flask(__name__, template_folder="../templates", static_folder="../static")
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from app import routes