"""Global project configuration."""


class Config(object):
    """Generic configuration class for default options."""

    DEBUG = True
    TESTING = False
    SECRET_KEY = b"""
        Q\x84\xa1\x8dQ\xfd\x1b\x06\xbd\xb9\x00G\xb1\xa5\x95\x91\x7f\xbf\xca\xf0=\xa1n{
        \x04\xdfT\x00\xdb2\xec\xf7\x96\x99\x18\xce\xba\xd2\xc7K\x9dS@\xb8\xc4\xae\xe9\xf4
    """

    CORS_ALLOW_ORIGIN = '*'
    CORS_ALLOW_METHODS = 'GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE'
    CORS_ALLOW_HEADERS = 'Content-Type, Accept, Authorization'


config = Config
