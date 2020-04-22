import json
import traceback
import logging

from app.song.models import Song
from app.song.views import create_song
from app.db import db

logging.basicConfig(level=logging.INFO)

#TODO: set youtube url, wrap in function
def exec(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

        for p in data['items']:
            session = db.session

            try:
                artist = p['track']['artists'][0]['name'] #TODO: concatenate artists
                title = p['track']['name']
                picture_url = p['track']['album']['images'][0]['url']

                #TODO: wrap this in its own function
                s = Song.query.filter_by(
                    title=title,
                    artist=artist
                ).first()
                if s is not None:
                    logging.warning(f'{artist} - {title} already exists')
                    continue

                s = Song( #TODO: set youtube url too
                    title=title,
                    artist=artist,
                    picture_url=picture_url,
                    spotify_meta=p,
                )
                session.add(s)
                session.commit()
                
                logging.info(f'{artist} - {title} CREATED!')

            except:
                logging.error(f'Failed to create {artist} - {title}')
                session.rollback()
                traceback.print_exc()
