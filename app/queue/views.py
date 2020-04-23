from flask import Blueprint, request, make_response
from app.queue.models import Queue
from app.db import db
from datetime import datetime
from app.song.models import Song
from app.user.models import User
from typing import List

blueprint = Blueprint('queue', __name__)


@blueprint.route('/queue/<uuid:song_id>', methods=['POST'])
def add_song(song_id: str):    
    song = Song.query.filter_by(id=song_id).first()
    if song is None:
        return make_response('song not found', 404)

    user_name = request.headers.get('user_name')
    user = User.query.filter_by(name=user_name).first()
    if user_name is None or user is None:
        return make_response('user not found', 404)

    add_song_to_queue(db.session, song, user)

    return make_response('song added', 200)
    

def add_song_to_queue(session, song: Song, by_user: User = None):
    """
    Adds song to queue
    """
    entry = Queue(
        song=song,
        user=by_user
    )
    session.add(entry)
    session.commit()
    