from flask import Flask

from {{ cookiecutter.project_slug }}.config import Config
from {{ cookiecutter.project_slug }}.routes import routes
from {{ cookiecutter.project_slug }}.teardown import shutdown_db_session


def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    for route in routes:
        app.add_url_rule(route[0], view_func=route[1])

    app.teardown_appcontext_funcs.extend([shutdown_db_session, ])

    return app
