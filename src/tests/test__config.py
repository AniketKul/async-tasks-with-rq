import unittest
from flask import current_app
from flask_testing import TestCase
from src.server import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('src.server.config.DevelopmentConfig')
        return app
    
    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertFalse(current_app.config['TESTING'])
        self.assertFalse(app.config['DEBUG'] is True)
        self.assertFalse(app.config['WTF_CSRF_ENABLED'] is False)
        
class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('src.server.config.TestingConfig')
        return app 

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['WTF_CSRF_ENABLED'] is False)

if __name__ == '__main__':
    unittest.main()