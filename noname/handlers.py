"""Module containing all handlers for the API."""
import logging
from datetime import datetime

import humanfriendly
from flask import g, request

from noname.responses import (
    ok,
    bad_request,
    unauthorized,
    forbidden,
    not_found,
    method_not_allowed,
    conflict,
    unprocessable_entity,
)


def register_handlers(app):
    """Register a bunch of handler on `app`."""
    @app.before_request
    def record_time():
        """Record the current time and store it in `g.request_start_time`."""
        g.request_start_time = datetime.utcnow()

    @app.after_request
    def add_cors_headers(response):
        """Add CORS to the headers of this request."""
        response.headers['Access-Control-Allow-Origin'] = app.config['CORS_ALLOW_ORIGIN']
        response.headers['Access-Control-Allow-Methods'] = app.config['CORS_ALLOW_METHODS']
        response.headers['Access-Control-Allow-Headers'] = app.config['CORS_ALLOW_HEADERS']
        return response

    @app.after_request
    def request_logging(response):
        """Log every request."""
        try:
            content_length = humanfriendly.format_size(response.calculate_content_length())
        except TypeError:
            content_length = 0
        request_time = datetime.utcnow() - g.request_start_time
        request_logger = logging.getLogger("request")
        request_logger.info(
            "{method:8s} {full_path} {status} ({content_length} in {time:.1f} ms)".format(
                method=request.method,
                full_path=request.full_path,
                status=response.status,
                content_length=content_length,
                time=request_time.total_seconds() * 1000,
            ))
        return response

    @app.errorhandler(400)
    def handle_bad_request(e):
        return bad_request(e.name)

    @app.errorhandler(401)
    def handle_unauthorized(e):
        return unauthorized(e.name)

    @app.errorhandler(403)
    def handle_forbidden(e):
        return forbidden(e.name)

    @app.errorhandler(404)
    def handle_not_found(e):
        if request.method == 'OPTIONS':
            return ok()
        return not_found(e.name)

    @app.errorhandler(405)
    def handle_method_not_allowed(e):
        return method_not_allowed(e.name)

    @app.errorhandler(409)
    def handle_conflict(e):
        return conflict(e.name)

    @app.errorhandler(422)
    def handle_unprocessable_entity(err):
        # webargs attaches additional metadata to the `data` attribute
        data = getattr(err, 'data', None)
        if data:
            # Get validations from the ValidationError object
            messages = data['messages']
        else:
            messages = ['Invalid request']
        return unprocessable_entity(messages)
