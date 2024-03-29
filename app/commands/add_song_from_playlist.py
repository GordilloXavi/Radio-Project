import traceback
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from app.song.models import Song
from app.song.views import create_song
from app.db import db
from app.song.views import create_song_from_query

logging.basicConfig(level=logging.INFO)

def exec(playlist_id: str):
    added_songs = 0
    total_songs = 0
    offset = 0
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    playlist = sp.playlist_tracks(playlist_id, limit=100, offset=offset)['items']
    while (len(playlist) > 0):
        for song in playlist:
            session = db.session
            total_songs += 1
            try:
                song_info = song['track']
                title = song_info['name']
                artist = song_info['artists'][0]['name']
                picture_url = song_info['album']['images'][0]['url']

                song_query = f'{title} {artist}'
                s = create_song_from_query(session, song_query)

                s.title = title
                s.artist = artist
                s.picture_url = picture_url
                s.spotify_meta = song_info

                session.commit()

                logging.info(f'{artist} - {title} CREATED!')
                added_songs += 1

            except:
                logging.error(f'Failed to create {artist} - {title}')
                session.rollback()
                traceback.print_exc()

        offset += 100
        playlist = sp.playlist_tracks(playlist_id, limit=100, offset=offset)['items']

    logging.info(f'Added {added_songs}/{total_songs} songs')
