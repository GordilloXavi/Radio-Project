import os
from dataclasses import dataclass


@dataclass
class Config:
    """
    Base class for configuration
    """
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    DB_PORT = 5432
    DB_HOST = 'db'


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
