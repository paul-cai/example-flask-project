"""
Holds configuration logic for different environments
"""
import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


def generate_postgres_uri():
    # Example postgres uri postgresql://scott:tiger@localhost/mydatabase
    # Database settings
    db_socket_dir = os.environ.get('DB_SOCKET_DIR', '/cloudsql')
    db_host = os.environ.get('DB_HOST', None)
    cloud_sql_connection_name = os.environ.get(
        'CLOUD_SQL_CONNECTION_NAME', 'climate-ai:us-central1:dashboard-db')
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    db_name = os.environ['DB_NAME']
    if db_host:
        return f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'
    else:
        return f'postgresql://{db_user}:{db_pass}@/{db_name}' \
               f'?host={db_socket_dir}/{cloud_sql_connection_name}'


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    #SQLALCHEMY_DATABASE_URI = generate_postgres_uri()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_template_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    #SQLALCHEMY_DATABASE_URI = generate_postgres_uri()
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_template_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = generate_postgres_uri()


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

# Instrumental key
INSTRUMENTAL_KEY = '25ac66f8d5a52214889988a50f16d4b5'

# ENV is mostly used for legacy implementations (instrumental naming, etc) not
# so much for loading configurations based on this.
ENV = os.environ.get('ENVIRONMENT', 'development')
