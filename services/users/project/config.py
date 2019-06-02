# services/users/project/config.py

import os

class BaseConfig:
	"""Base configuration"""
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'i_dont_want_it'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(BaseConfig):
	"""Development configuration"""
	pass


class TestingConfig(BaseConfig):
	"""Testing configuration"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
	"""Production configuration"""
	pass
