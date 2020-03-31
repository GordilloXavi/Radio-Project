from flask import Blueprint, redirect, request

blueprint = Blueprint('url_shortener', __name__)


@blueprint.route('/ig', methods=['GET'])
def instagram():
    return redirect('https://www.instagram.com/xavigordill0/', code=302)

@blueprint.route('/git', methods=['GET'])
def github():
    return redirect('https://github.com/GordilloXavi', code=302)

@blueprint.route('/spoti', methods=['GET'])
def spoti():
    return redirect('https://open.spotify.com/user/xgordillo00?si=H4NtAiyjQeijZ4-jPwhXDw', code=302)

@blueprint.route('/fenas', methods=['GET'])
def fenas():
    return redirect('spoti.fi/2zkS84e', code=302)
    
@blueprint.route('/spoti/pl/<playlist_name>', methods=['POST', 'GET'])
def spoti_playlist(playlist_name: str):
    """
    TODO:
    persist an url (or playlist_name) associated with its redirect link in db
    """
    if request.method == 'POST':
        return 'WIP'
    
    if playlist_name == 'fenas':
        return fenas()
    if playlist_name.lower() == 'chill':
        return redirect('https://open.spotify.com/playlist/65wgLG8gaRYDqpaada7yLI?si=H4NtAiyjQeijZ4-jPwhXDw', code=302)
    
    return spoti()