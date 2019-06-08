# services/users/manage.py

import unittest
import sys 

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
	db.drop_all()
	db.create_all()
	db.session.commit()

"""Runs the tests

Runs the tests without code coverage
"""
@cli.command('test')
def test():
	tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	sys.exit(result)


"""Populate the database

Populates the database with some data
"""
@cli.command('seed_db')
def seed_db():
	"""Seeds the database."""
	db.session.add(User('michael', 'michael@mherman.org'))
	db.session.add(User('fletcher', 'fletcher@notreal.com'))
	db.session.commit()

if __name__ == '__main__':
	cli()