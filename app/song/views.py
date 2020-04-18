from flask import Blueprint, request

blueprint = Blueprint('song', __name__)

@blueprint.route('/song/<id>', methods=['GET', 'POST'])
def user(id: str):
    session = db.session
    if request.method == 'GET':
        return 'got song!'
    
    if request.method == 'POST':
        return 'posted song!'