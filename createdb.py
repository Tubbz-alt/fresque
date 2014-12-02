#!/usr/bin/python

## These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.8', 'jinja2 >= 2.4']
import pkg_resources

from fresque import APP
from fresque.lib import model

path_alembic = None
if 'PATH_ALEMBIC_INI' in APP.config \
        and APP.config['PATH_ALEMBIC_INI']:
    path_alembic = APP.config['PATH_ALEMBIC_INI']
model.create_tables(APP.config['SQLALCHEMY_DATABASE_URI'], path_alembic, True)
