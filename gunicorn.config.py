""" File that contains gunicorn startup configurations. """
import multiprocessing
import os

workers = multiprocessing.cpu_count() * 2 + 1
threads = os.environ.get("GUNICORN_THREADS", 8)
loglevel = os.environ.get("GUNICORN_LOGLEVEL", "INFO")
errorlogfile = "./logs/gunicorn_error.log"
accesslogfile = "./logs/gunicorn_access.log"
capture_output = True
reload = True
