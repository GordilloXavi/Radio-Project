from flask import Blueprint
import click

blueprint = Blueprint('com', __name__)

@blueprint.cli.command('add_songs')
@click.argument('file_name')
def add_songs_from_json(file_name):
    """
    Usage:
    flask com add_songs songs.json
    """
    from app.commands.add_songs_from_json import exec
    exec(file_name)
