.ONESHELL:

.PHONY: clean install tests run migration db_init lint pr all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements/requirements.txt;

tests:
	. venv/bin/activate; \
	flask test

run:
	export FLASK_ENV=development; \
	export FLASK_APP=manage.py; \
	. venv/bin/activate; \
	flask run

migration:
	. venv/bin/activate; \
	export FLASK_APP=manage.py; \
	flask db migrate

db_init:
	. venv/bin/activate; \
	export FLASK_APP=manage.py; \
	flask db init

lint:
	. venv/bin/activate; \
	pylint app --rcfile=.pylintrc

pr: lint tests

all: clean install tests run
