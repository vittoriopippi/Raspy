import os
import time
import telepot
from hdbot import HDbot
import hdtscraper

try:
    RASPYMOVIEBOT_TOKEN = os.environ['RASPYMOVIEBOT_TOKEN']
    RASPYMOVIEBOT_PASSWORD = os.getenv('RASPYMOVIEBOT_PASSWORD', 'alpine')
    HDTORRENT_USERNAME = os.environ['HDTORRENT_USERNAME']
    HDTORRENT_PASSWORD = os.environ['HDTORRENT_PASSWORD']
except KeyError:
    print('The enviroment variables needed are not found')
    variables = ['RASPYMOVIEBOT_TOKEN', 'RASPYMOVIEBOT_PASSWORD', 'HDTORRENT_USERNAME', 'HDTORRENT_PASSWORD']
    [print(f'{var}\t= {os.getenv(var)}') for var in variables]
    exit(1)

bot = telepot.Bot(RASPYMOVIEBOT_TOKEN)
hdbot = HDbot(bot, HDTORRENT_USERNAME, HDTORRENT_PASSWORD, RASPYMOVIEBOT_PASSWORD)
print ('Listening...')

# Keep the program running.
while 1:
    hdbot.reload()
    time.sleep(60)