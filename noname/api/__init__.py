"""Entry point for the API blueprint."""
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='')

from noname.api import (  # noqa E402
    echo,
)
