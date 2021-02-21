import time
import telepot
from hdbot import HDbot
import hdtscraper

try:
    from settings import *
except ImportError:
    print("The bot to work properly needs the file 'settings.py'.")
    print("To create it, you can use the file 'settings_template.py' as template.")
    exit(1)

bot = telepot.Bot(RASPYMOVIEBOT_TOKEN)
hdbot = HDbot(bot, HDTORRENT_USERNAME, HDTORRENT_PASSWORD, RASPYMOVIEBOT_PASSWORD)
hdbot.torrents_folder = TORRENT_FOLDER
hdbot.downloading_folder = INCOMPLETE_FOLDER
hdbot.completed_folder = COMPLETED_FOLDER
hdbot.uploading_folder = UPLOADING_FOLDER

hdbot.start_loop()
print ('Listening...')

# Keep the program running.
while 1:
    hdbot.reload()
    time.sleep(LOOP_TIME)