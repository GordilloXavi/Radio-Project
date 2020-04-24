import youtube_dl
import traceback

def get_youtube_meta(query: str) -> dict:
    """
        Queries youtube for the first song matching query search
        Returns a dict containing the following fields:
            video_url: str
            categories: list[str]
            title: str
            thumbnail_picture: str
            duration: int
            song_name: str
            artist: str
            album: str
    """
    ydl_opts = {
        'write_info_json': True,
        'no_playlist': True,
        'skip_download': True,
        'forcejson': True,
        'noplaylist': True,
        'writeinfojson': True,
        'quiet': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            data = ydl.extract_info(
                f'ytsearch:{query} audio',
                download=False
            )['entries'][0]

        except: #TODO: log error
            print('ERROR!!!')
            traceback.print_exc()
            return None

        return {
            'video_url': data.get('webpage_url'),
            'categories': data.get('categories'),
            'title': data.get('title'),
            'thumbnail_picture': data.get('thumbnail'),
            'duration': data.get('duration'),
            'song_title': data.get('track'),
            'album': data.get('album'),
            'artist': data.get('artist'),
        }
