"""This file defines asynchronous tasks for the uwsgi.

See http://uwsgi-docs.readthedocs.io/en/latest/PythonDecorators.html .
And http://uwsgi-docs.readthedocs.io/en/latest/Spooler.html .
"""

import os
from noname import create_app
from uwsgidecorators import timer


app = create_app()


# The only thing the `spooler` does - it executes the function in a separate special process, not
# in the general uwsgi-workers.
@timer(5, target='spooler')
def recurring_print(signum):
    """Simple recurring task test."""
    with app.app_context():
        pass

