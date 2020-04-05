import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base Configuation
    """
    WTF_CSRF_ENABLED = True
    REDIS_URL = 'redis://redis:6379/0'
    QUEUES = ['default']

class DevelopmentConfig(BaseConfig):
    """
    Development Configuation
    """
    WTF_CSRF_ENABLED = False

class WTF_CSRF_ENABLED(BaseConfig):
    """
    Testing Configuation
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
