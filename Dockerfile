# pull official base image
FROM python:3.8.12-buster

# install postgresql in cas needed
RUN apt-get update && apt-get -y install libpq-dev build-essential

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## Pip 22 is used due to conflicts with pip tools
## might not be the case in future
# install pip tools for pip compile
RUN pip install pip-tools &&\
    pip install 'pip<22'


# Change server timezone, not necessary but helps with logging
RUN cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime

# copy project
COPY . /usr/src/app/

## We can either compile the requirements each time from a set of production reqs
## or we can use the ones we already compilded
# compile and install dependencies
#RUN pip-compile ./requirements/production.in --output-file ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt

ENTRYPOINT gunicorn --bind :$PORT -c ./gunicorn.config.py --timeout 0 manage:app
