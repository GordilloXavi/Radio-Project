import os
from dataclasses import dataclass


@dataclass
class Config:
    """
    Base class for configuration
    """


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
