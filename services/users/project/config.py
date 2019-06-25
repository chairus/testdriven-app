# services/users/project/config.py

import os


class BaseConfig:
	"""Base configuration """
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'i_dont_want_it'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	DEBUG_TB_ENABLED = False
	DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
	"""Development configuration"""    
	DEBUG_TB_ENABLED = True


"""Testing configuration Contains configuration for testing environment"""
class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


"""Production configuration Contains configuration for production environment"""
class ProductionConfig(BaseConfig):
    pass

