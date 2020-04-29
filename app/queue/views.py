from flask import Blueprint, request, make_response
#from app.sockets import socketio
from flask_socketio import emit
from app.queue.models import Queue
from app.db import db
from datetime import datetime
from app.song.models import Song
from app.user.models import User
from typing import List
import json
import traceback

blueprint = Blueprint('queue', __name__)


#FIXME: implement with sockets!!
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

    queue = get_current_queue(5)
    queue_data = {'entries': [q.to_dict() for q in queue]}
    data = json.dumps(queue_data)

    emit(
        'queue_update', 
        data,
        json=True,
        namespace='/queue',
        broadcast=True
    )
 
    return make_response('song added', 200)

@blueprint.route('/queue/<int:max_entries>', methods=['get'])
def get_queue_element(max_entries: int):
    if max_entries > 50 or max_entries < 0:
        return make_response('max entries: 50')
        
    try:
        entries = get_current_queue(max_entries=max_entries)
        queue_data = {'entries': [q.to_dict() for q in entries]}
        
        return make_response(queue_data, 200)
    
    except:
        #TODO: log error
        traceback.print_exc()
        return make_response('summ happened', 500)
    

def add_song_to_queue(session, song: Song, by_user: User = None):
    """
    Adds song to queue
    TODO: aviod adding songs with no youtube link or no title
    TODO: aviod adding a song that was played recently
    TODO: aviod adding songs with a duratrion > 15 min
    """
    try:
        entry = Queue(
            song=song,
            user=by_user
        )
        session.add(entry)
        session.commit()
    except: #TODO: log error
        session.rollback()
    
def get_current_queue(max_entries: int  = 5) -> List[Queue]:
    entries = []

    user_request_entries = Queue.query.filter_by(
        played=False,
        user_request=True
        ).limit(max_entries).all()

    diff = max_entries - len(user_request_entries)

    if diff > 0:
        other_entries = Queue.query.filter_by(
            played=False,
            user_request=False
        ).limit(diff).all()

        entries = user_request_entries + other_entries

    return entries
        
