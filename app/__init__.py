"""Initialize Flask app."""

from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from pathlib import Path

import app.adapters.repository as repo

from app.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    app = Flask(__name__)


    csrf = CSRFProtect()
    csrf.init_app(app)

    
    app.config.from_object('config.DevConfig')


    # Data Path load data
    data_path = Path('music') / 'adapters' / 'data'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # loads the memory repo
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from app.blueprints.app_blueprints import app_blueprint
        app.register_blueprint(app_blueprint)

    return app
