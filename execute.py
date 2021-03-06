import unittest
import redis
from rq import Connection, Worker
from flask.cli import FlaskGroup
from src.server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    """
    runs unittests without test coverage
    """
    tests = unittest.TestLoader().discover('src/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('run_worker')
def run_worker():
    redis_url = app.config['REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config['QUEUES'])
        worker.work()

if __name__ == '__main__':
    cli()