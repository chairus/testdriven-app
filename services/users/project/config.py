# services/users/project/config.py

import os

"""Base configuration

Common configuration for all types of environment"""
class BaseConfig:
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'i_dont_want_it'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


"""Development configuration

Contains configuration for development environment"""
class DevelopmentConfig(BaseConfig):
	pass


"""Testing configuration

Contains configuration for testing environment"""
class TestingConfig(BaseConfig):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


"""Production configuration

Contains configuration for production environment"""
class ProductionConfig(BaseConfig):
	pass

