from flask import Flask


application = Flask(__name__)
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

from app import routes