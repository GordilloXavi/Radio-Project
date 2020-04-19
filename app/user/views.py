from flask import Blueprint, request, make_response
from app.user.models import User
from app.db import db

blueprint = Blueprint('user', __name__)


@blueprint.route('/user/<user_name>', methods=['GET', 'POST'])
def user(user_name: str):
    session = db.session
    if request.method == 'GET':
        user = get_user_info(user_name)

        if user is None:
            return 'not found'
        
        return make_response(user.to_dict())
    
    if request.method == 'POST':
        user = create_new_user(session, user_name)

        if user is None:
            return 'user already exists'
            
        return make_response(user.to_dict())

def get_user_info(user_name: str):
    """
    Returns the user's information.
    If the user deos not exist, returns an error.
    """
    return User.query.filter_by(name=user_name.lower()).first()


def create_new_user(session, user_name: str) -> User:
    """
    Creates a new user with the specified user name.
    If the user already existed, returns an error.
    """
    user = User.query.filter_by(name=user_name.lower()).first()
    if user is not None:
        return None

    new_user = User(name=user_name)
    session.add(new_user)
    session.commit()

    return new_user