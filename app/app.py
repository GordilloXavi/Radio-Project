from flask import Flask
from app.config import Config, ProdConfig

def create_app(config_object: Config = ProdConfig) -> Flask:
    """
    Creates and configures the app
    Args:
        config_object (Config)
    Returns:
        Flask application
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    @app.route('/health') #TODO:  move to routes folder
    def health():
        return 'Healthy :)'

    return app