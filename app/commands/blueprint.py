from flask import Blueprint
import click

blueprint = Blueprint('com', __name__)

@blueprint.cli.command('add_songs')
@click.argument('string')
def add_songs(string: str):
    """
    flask com add_songs <filename>.json
    or
    flask com add_songs <playlist_id>
    """
    if (string.endswith('.json')):
        from app.commands.add_songs_from_json import exec
        exec(string)
    else:
        from app.commands.add_song_from_playlist import exec
        exec(string)

@blueprint.cli.command('update_queue')
def update_queue():
    """
    flask com update_queue
    """
    from app.commands.update_queue import exec
    exec()
