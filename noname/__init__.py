"""This package contains the `noname` app including everything which is noname.

This particular file exports the applications factory.
"""

from flask import Flask


def create_app():
    """Flask app factory function."""
    app = Flask(__name__)

    from noname.config import config
    app.config.from_object(config)

    # Initialize handlers
    from noname.handlers import register_handlers
    register_handlers(app)

    # Initialize blueprints
    from noname.api import api
    app.register_blueprint(api)

    return app
