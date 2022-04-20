import os
import unittest

from flask import g
from instrumental_agent import Agent

from app import blueprint
from app.main import create_app
from app.main.config import ENV, INSTRUMENTAL_KEY

app = create_app(os.getenv('CONFIG_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()


@app.cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@app.before_request
def before_request_func():
    g.setdefault('LOGGER', Agent(INSTRUMENTAL_KEY, enabled=True, secure=False))


@app.after_request
def after_request_func(response):
    SERVICE_NAME = "Placeholder"
    g.get('LOGGER').increment(f'{ENV}.{SERVICE_NAME}.response.{str(response.status_code)}')
    return response


if __name__ == '__main__':
    app.run()
