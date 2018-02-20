"""A simple echo route."""
from flask import request

from noname.api import api
from noname.responses import ok


@api.route('/', methods=['GET'])
def default():
    """Echo the parameters of the request."""
    return ok(data=request.args)
