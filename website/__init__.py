from flask import Flask
from os import path
from .views import UPLOAD_FOLDER

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    from .views import views
    app.register_blueprint(views)
    app.config['SECRET_KEY'] = 'thisissupersecret'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    return app

