HDTORRENT_USERNAME = '...'
HDTORRENT_PASSWORD = '...'
RASPYMOVIEBOT_TOKEN = '...'
RASPYMOVIEBOT_PASSWORD = '...'
TMDB_KEY_v3 = '...'
TMDB_KEY_v4 = '...'
TORRENT_FOLDER = './Torrents'
INCOMPLETE_FOLDER = './Incomplete'
COMPLETED_FOLDER = './Completed'
UPLOADING_FOLDER = './Uploading'
LOOP_TIME = 300

from pathlib import Path
Path(TORRENT_FOLDER).mkdir(parents=True, exist_ok=True)
Path(INCOMPLETE_FOLDER).mkdir(parents=True, exist_ok=True)
Path(COMPLETED_FOLDER).mkdir(parents=True, exist_ok=True)
Path(UPLOADING_FOLDER).mkdir(parents=True, exist_ok=True)