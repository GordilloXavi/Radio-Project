from flask import Blueprint, make_response
from app.db import db
from typing import List
from app.song.models import Song
from sqlalchemy import func
from app.utils.youtube import get_youtube_meta
import traceback

blueprint = Blueprint('song', __name__)

@blueprint.route('/song/<query>', methods=['POST'])
def create(query: str):
    try:
        session = db.session
        song = create_song_from_query(session, query)

        if song is None:
            return make_response('song matching query not found', 404)

        return make_response(song.to_dict(), 201)

    except: #TODO: return proper response based on custom exceptions
        return make_response('server error', 500)
    

def create_song_from_query(session, query: str) -> Song:
    """
    Creates a song from a youtube query if the query is successful;
    Otherwise, returns None
    """
    youtube_data = get_youtube_meta(query)

    if youtube_data is None:
        return None

    youtube_title = youtube_data.pop('title')
    youtube_url = youtube_data.pop('video_url')
    thumbnail = youtube_data.pop('thumbnail_picture')
    duration = youtube_data.pop('duration')
    meta = youtube_data

    song = Song.query.filter_by(
        yt_title=youtube_title,
        yt_url=youtube_url
    ).first()

    if song is not None:
        return song

    song = Song(
        yt_title=youtube_title,
        yt_url=youtube_url,
        yt_thumbnail_url=thumbnail,
        duration=duration,
        yt_meta=meta
    )

    try:
        session.add(song)
        session.commit()
        return song

    except:
        #TODO: log error
        traceback.print_exc()
        session.rollback()
        return None


def create_song( #TODO:
    session,
    title: str = None,

) -> Song:
    """
    Attempts to crete a song with the given arguments if no similar song exists
    """
    pass
