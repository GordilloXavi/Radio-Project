from flask import Flask
from app.config import Config, ProdConfig

from app.url_shortener.views import blueprint as url_shortener_bp

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

    @app.route('/health')
    def health():
        return 'Healthy :)', 200

    app.register_blueprint(url_shortener_bp)

    return app