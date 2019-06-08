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
@cli.command()
def test():
	tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	sys.exit(result)

if __name__ == '__main__':
	cli()