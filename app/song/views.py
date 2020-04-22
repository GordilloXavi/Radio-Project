from flask import Blueprint, request
from app.db import db
from typing import List
from app.song.models import Song, Category, SongCategory
from sqlalchemy import func
import youtube_dl

blueprint = Blueprint('song', __name__)





def create_song( #TODO:
    session,
    title: str,
    artist: str,
    categories: List[Category] = None,
    youtube_url: str = None,
    picture_url: str = None,
    spotify_meta: dict = None
    ):
    song = Song.query.filter(
        func.lower(Song.title) == func.lower(title),
        func.lower(Song.artist) == func.lower(artist)
    ).first()

    if song is not None:
        return

    song = Song(
        title=title,
        artist=artist
    )
    for category in categories:
        sc = SongCategory(
            song=song,
            category=category
        )
        song.categories.append(sc)
        session.add(sc)
    
    session.add(song)
    session.commit()

def get_song_from_query(session, query: str): #FIXME!!!
    """
        Query for a similar song. If it exists: return it
        Download song data with youtbe-dll
        Persist song
        Delete json data
        Return song
    """
    ydl_opts = { #FIXME: tune parameters!!
        'output': 'current_video',#FIXME: extemsion
        'write-info-json': True,
        'max-filesize': '1000k',
        'no-playlist': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'skip-download': True, #Do not download the video
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: #TODO: encapsulate in own class
        ydl.download([f'ytsearch:{query} audio'])