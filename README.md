[![Build Status](https://travis-ci.org/fedora-infra/fresque.svg?branch=master)](https://travis-ci.org/fedora-infra/fresque)

Fresque
=======
Fedora Review Server

Installation
----------------
To download the project, open your terminal and type the following command

```bash
	$ git clone https://github.com/fedora-infra/fresque.git
	$ cd fresque
	$ python setup.py install
```
It will clone and install the project on your local machine

Dependencies
------------
Fresque is a [Flask] application. The review data is stored into a relational database
using [SQLAlchemy] as Object Relational Mapper and [alembic] to handle database
schema changes.

The dependecies can be found in [requirements.txt](https://github.com/fedora-infra/fresque/blob/master/requirements.txt)

Running a development instance:
-------------------------------
First lets make a seperate virtual environment for the project
to avoid conflicts of its dependecy with other python packages.
after that install [virtualenv wrapper] which provides better CLI interface
for the [virtualenv].

```bash
	$ yum install python-virtualenv
	$ yum install python-virtualenvwrapper
```
*Note: If you are using fedora >= 22, use `dnf` instead of `yum`*

Close and reopen your terminal.

Create a seperate virtualenv for this project.

```bash
	// create a virtualenv named fresque
	$ mkvirtualenv fresque
	// if not automatically switched to fresque virtualenv, then type
	$ workon fresque
	// now your bash prompt line will change to
	(fresque) $
```

Now clone the source:

```bash
	$ git clone https://github.com/fedora-infra/fresque.git
	$ cd fresque
	$ pip install -r requirements.txt
	// set up the database before running the server
	$ python createdb.py
	// now start the server
	$ python runserver.py
```
Thats all now head to [http://localhost:5000](http://localhost:5000)

Testing
-------

Currently fresque doesn't have any unit tests.


License:
--------
This project is licensed GPLv3+.

[Flask]:http://flask.pocoo.org/
[SQLAlchemy]:http://www.sqlalchemy.org/
[alembic]:https://bitbucket.org/zzzeek/alembic
[virtualenv]:https://virtualenv.pypa.io/en/latest/
[virtualenv wrapper]:https://virtualenvwrapper.readthedocs.org/en/latest/
