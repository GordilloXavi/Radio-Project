import os
from dataclasses import dataclass


@dataclass
class Config:
    """
    Base class for configuration
    """
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', 5000)

    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    DB_PORT = 5432
    DB_HOST = 'db'

    SECRET_KEY = os.environ.get('SECRET_KEY')


@dataclass
class DevConfig(Config):
    """
    Configuration for development env
    """


@dataclass
class ProdConfig(Config):
    """
    Configuration for production env
    """
