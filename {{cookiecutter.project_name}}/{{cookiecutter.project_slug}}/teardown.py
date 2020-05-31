from {{ cookiecutter.project_slug }}.db import db_session


def shutdown_db_session(exception=None):
    db_session.remove()
