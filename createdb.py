#!/usr/bin/python

## These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.8', 'jinja2 >= 2.4']
import pkg_resources

from fresque import APP
from fresque.lib.database import create_tables

create_tables(APP.config, True)
