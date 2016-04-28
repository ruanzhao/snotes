
from flask import Flask

from snotes.config import DefaultConfig
from snotes.database import db
from snotes.extensions import login_manager
from snotes.home.models import User


__all__ = ['create_app']


def create_app(app_name=None, config=None):
    """ creae a flask app """
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name)

    _register_blueprints(app)
    _configure_app(app)
    _configure_extensions(app)

    return app


def _register_blueprints(app):
    from snotes.home import home
    from snotes.note import note
    app.register_blueprint(home, url_prefix=None)
    app.register_blueprint(note, url_prefix='/note')

def _configure_app(app, config=None):
    """ Configure app. """
    app.config.from_object(DefaultConfig)

def _configure_extensions(app):
    db.init_app(app)

    login_manager.login_view = '/home/login'
    login_manager.refresh_view = '/home/loign'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
        
    login_manager.init_app(app)


