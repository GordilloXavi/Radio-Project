from flask import Blueprint, request, make_response
from app.queue.models import Queue
from app.db import db
from datetime import datetime
from app.song.models import Song
from typing import List

blueprint = Blueprint('queue', __name__)


@blueprint.route('/queue/<max_songs>', methods=['GET', 'POST'])
def queue(max_songs: int):
    session = db.session
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        pass

@blueprint.route('/queue/', methods=['POST'])
def add_song():
    pass
    


def get_queue_songs(max_songs: int = 5) -> List[Song]:
    """
    Returns the top songs from the queue
    """
    requested_songs = Queue.query.filter_by(played=False, user_request=True) \
        .order_by(Queue.position.desc()).limit(max_songs)

    songs_left = max_songs - requested_songs.count()

    if songs_left == 0:
        return requested_songs.all()
    
    songs = requested_songs = Queue.query.filter_by(played=False, user_request=False) \
        .order_by(Queue.position.desc()).limit(songs_left).all()
    
    songs.append(requested_songs.all())

    return songs

def pop_queue(session):
    """
    Marks the first song of the queue as played
    """
    last_song = Queue.query.filter_by(played=False).order_by(Queue.position.asc()).first()
    
    if last_song is None:
        return

    last_song.played_at = datetime.now()
    last_song.played = True

    session.commit() # make sure this indeed updates the row

def add_to_queue(session, song: Song, user_request: bool = False):
    """
    Adds song to queue
    """
    entry = Queue(
        song=song,
        user_request=user_request
    )
    session.add(entry)
    session.commit()
    