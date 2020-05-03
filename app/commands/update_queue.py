

import traceback
import logging
from time import sleep
from random import randint
from app.queue.views import add_song_to_queue
from flask_socketio import emit
from datetime import datetime

from app.db import db
from app.queue.models import Queue, QueueStatus
from app.song.models import Song
from app.queue.views import get_current_queue
import json

logging.basicConfig(level=logging.INFO)

def exec():
    """
    #TODO: account for time taken in operations; mark the video as stopped before the duration is actually over
    every second, update current time and check it it is < duration
    if it is == duration:
        mark the song as played
        add a random (has artist, video and link) song to the queue
        mark the next song a playing
        emit a queue_updated event

    """
    while (True):
        current_entry = Queue.query.filter_by(status=QueueStatus.PLAYING).first()

        if current_entry is None:
            logging.warning('There are no songs in the queue')
            play_next_song(db.session)
            sleep(1)
            continue

        if is_finished(current_entry): #FIXME: do transactionally with the same session
            logging.info("Current song finihed playing")

            mark_entry_as_finished(db.session, current_entry)

            add_random_song_to_queue(db.session)

            play_next_song(db.session)

            notify_queue_change()

        else:
            update_entry_time(db.session, current_entry)
            sleep(1)

def is_finished(entry: Queue) -> bool:
    current_time = entry.current_second
    duration = entry.song.duration

    return not (current_time < duration) #TODO: maybe give it a second of margin
            
def mark_entry_as_finished(session, entry: Queue) -> None:
    entry.status = QueueStatus.PLAYED
    entry.current_second = 0
    
    try:
        session.commit()
        logging.info(f'Song {entry.song.id} finished playing')

    except:
        logging.exception('Error updating queue:')
        traceback.print_exc

def add_random_song_to_queue(session) -> None:
    songs = Song.query.filter(
        Song.title is not None,
        Song.artist is not None,
        Song.yt_url is not None,
        Song.duration is not None,
    ).all()

    songs_count = len(songs)
    print(f'Numer of songs: {len(songs)}')
    if songs_count == 0:
        logging.info('There are no songs')
        return
    
    rand = randint(0, songs_count)
    random_song = songs[rand]

    add_song_to_queue(session, random_song)

    logging.info(f'Added new song to queue: {random_song.id}')

def play_next_song(session) -> None:
    playing_song = Queue.query.filter_by(status=QueueStatus.PLAYING).first()
    
    if playing_song is not None:
        logging.warning("Attempted to play a new song while another one is playing")
        return

    queue = get_current_queue(max_entries=1)

    if len(queue) == 0:
        logging.info("No more songs to play")
        return

    next_entry = queue[0]

    next_entry.played_at = datetime.now()
    next_entry.status = QueueStatus.PLAYING

    requested_by = next_entry.user.name if next_entry.user else 'Nobody'

    try:
        session.commit()
        logging.info(f'Now playing: {next_entry.song.id}, requested by {requested_by}')

    except:
        logging.exception('Error playing next song:')
        traceback.print_exc()
    

def notify_queue_change() -> None:
    queue = get_current_queue(max_entries=50)
    queue_data = {'entries': [q.to_dict() for q in queue]}
    data = json.dumps(queue_data)

    emit(
        'queue_update', 
        data,
        json=True,
        namespace='/queue',
        broadcast=True
    )

def update_entry_time(session, entry: Queue) -> None:
    if entry.current_second > entry.song.duration:
        logging.warning("Current song second is greater than its duration")
        return

    logging.info(f'{entry.current_second}/{entry.song.duration}')
    entry.current_second += 1
    session.commit()
