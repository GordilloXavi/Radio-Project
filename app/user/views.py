from flask import Blueprint, request
from app.user.models import User
from app.db import db

blueprint = Blueprint('user', __name__)


@blueprint.route('/user/<user_name>', methods=['GET', 'POST'])
def user(user_name: str):
    session = db.session
    if request.method == 'GET':
        return get_user_info(session, user_name)
    
    if request.method == 'POST':
        return create_new_user(session, user_name)

def get_user_info(session, user_name: str):
    """
    Returns the user's information.
    If the user deos not exist, returns an error.
    """
    pass

def create_new_user(session, user_name: str) -> str:
    """
    Creates a new user with the specified user name.
    If the user already existed, returns an error.
    """
    user = User.query.filter_by(name=user_name.lower()).first()
    if user is not None:
        return f'User with name {user_name} already exists' #FIXME:

    new_user = User(name=user_name)
    session.add(new_user)
    session.commit()

    return f'User {new_user.name} created with id {new_user.id}' #FIXME: