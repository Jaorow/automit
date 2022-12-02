"""Initialize Flask app."""

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from pathlib import Path




def create_app(test_config=None):
    app = Flask(__name__)


    csrf = CSRFProtect()
    csrf.init_app(app)

    
    app.config.from_object('config.DevConfig')




    with app.app_context():
        from app.blueprints.app_blueprints import app_blueprint
        app.register_blueprint(app_blueprint)

    return app
