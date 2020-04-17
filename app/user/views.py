from flask import Blueprint, request

blueprint = Blueprint('url_shortener', __name__)


@blueprint.route('/user/<user_name>', methods=['GET', 'POST'])
def user(user_name: str):
    from start import db

    if request.method == 'GET':
        return get_user_info(user_name)
    
    if request.method == 'POST':
        return create_new_user(user_name)

def get_user_info(user_name: str):
    """
    Returns the user's information.
    If the user deos not exist, returns an error.
    """
    pass

def create_new_user(user_name: str):
    """
    Creates a new user with the specified user name.
    If the user already existed, returns an error.
    """
    pass