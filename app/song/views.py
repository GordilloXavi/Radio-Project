from flask import Blueprint, request
from app.db import db
from typing import List
from app.song.models import Song, Category, SongCategory
from sqlalchemy import func

blueprint = Blueprint('song', __name__)





def create_song(
    session,
    title: str,
    artist: str,
    categories: List[Category]
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
