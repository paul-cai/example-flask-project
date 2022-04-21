# flask_template
Flask template to create flask apps faster.

## Instalation
Install virtualenv `pip install virtualenv`
Run the script in 'install' inside the Makefile to create the venv and activate it

## Developing
To run the server, use `python manage.py run`
To run tests, use `python manage.py test`
To lint use  `pylint --rcfile=.pylintrc <file or directory>`


If you don't need a relational database, remove the `Migration`, `db`, and `SQLAlchemy` components.code
