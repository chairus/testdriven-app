# services/users/project/config.py

import os

class BaseConfig:
	"""Base configuration"""
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'i_dont_want_it'


class DevelopmentConfig(BaseConfig):
	"""Development configuration"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
	"""Testing configuration"""
	TESTING = True
	SQLAEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
	"""Production configuration"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
