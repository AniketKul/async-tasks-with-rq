from flask_testing import TestCase
from src.server import create_app

app = create_app()

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('src.server.config.TestingConfig')
        return app
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
