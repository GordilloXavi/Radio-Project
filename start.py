from flask import Flask

from flask.helpers import get_debug_flag

from app.config import Config, DevConfig, ProdConfig
from app.db import db
from app.user.views import blueprint as user_blueprint
from app.song.views import blueprint as song_blueprint
from app.queue.views import blueprint as queue_blueprint
from app.commands.blueprint import blueprint as commands_blueprint
from app.sockets import socketio

def get_databasse_uri(app: Flask) -> str:
    user = app.config.get('DB_USER')
    passwd = app.config.get('DB_PASSWORD')
    host = app.config.get('DB_HOST')
    port = app.config.get('DB_PORT')
    db = app.config.get('DB_NAME')
    return f'postgresql://{user}:{passwd}@{host}:{port}/{db}'

def create_categories(session):
    from app.song.models import Category, CategoryType

    try:
        for c in CategoryType:
            category = Category(category=c.value)
            session.add(category)

        session.commit()
    except:
        session.rollback()

def init_database(app): #FIXME: must be a better way to do this
    db.init_app(app)
    from app.song.models import Song, SongCategory, Category
    from app.user.models import User
    with app.app_context():
        db.create_all()
        create_categories(db.session) #FIXME: move elsewhere, maybe commands


def create_app(config_object: Config = ProdConfig):
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
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/health')
    def health():
        return 'Healthy :)', 200

    app.register_blueprint(user_blueprint) #TODO: add prefix
    app.register_blueprint(song_blueprint)
    app.register_blueprint(queue_blueprint)
    app.register_blueprint(commands_blueprint)

    init_database(app)
    
    socketio.init_app(app)

    return app


config = DevConfig if get_debug_flag() else ProdConfig
app = create_app(config)


if __name__ == "__main__":
    app.run()
