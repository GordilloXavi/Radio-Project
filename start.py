from flask.helpers import get_debug_flag
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

from app.app import create_app
from app.config import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=['3/second']    
)
db = SQLAlchemy(app)

db.create_all() # FIXME: do this gotta go here?

if __name__ == "__main__":
    app.run()
