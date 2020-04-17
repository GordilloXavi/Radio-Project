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

    app.config['SQLALCHEMY_DATABASE_URI'] = get_databasse_uri(app)

    @app.route('/health')
    def health():
        return 'Healthy :)', 200

    app.register_blueprint(url_shortener_bp)

    return app

def get_databasse_uri(app: Flask) -> str:
    user = app.config.get('DB_USER')
    passwd = app.config.get('DB_PASSWORD')
    host = app.config.get('DB_HOST')
    port = app.config.get('DB_PORT')
    db = app.config.get('DB_NAME')
    return f'postgresql://{user}:{passwd}@{host}:{port}/{db}'
