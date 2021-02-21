from hdtscraper import hdtscraper
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.parse import quote

class HDbot:
    owner = 214833693
    last_movie_id = 0
    locked = True
    movie_history = {}
    torrents_dst = '.'

    def __init__(self, bot, username, password, unlock_password):
        self.bot = bot
        self.username = username
        self.password = password
        self.unlock_password = unlock_password
        self.scraper = hdtscraper(username, password)
        MessageLoop(self.bot, {'chat': self.on_chat_message, 'callback_query': self.on_callback_query}).run_as_thread()
    
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(msg)
        if content_type == 'text' and msg['text'].startswith(r'\unlock '):
            self.unlock(msg)

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, query_data)

        movie = self.movie_history[query_data]['movie']
        message = self.movie_history[query_data]['message']
        self.scraper.download_torrent(movie, self.torrents_dst)

        msg_id = telepot.message_identifier(message)
        self.bot.editMessageReplyMarkup(msg_id)

        self.bot.answerCallbackQuery(query_id, text='Downloading...')

    def unlock(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        assert content_type == 'text' and msg['text'].startswith(r'\unlock ')
        self.bot.deleteMessage(telepot.message_identifier(msg))
        if msg['text'][len(r'\unlock '):] == self.unlock_password:
            self.owner = chat_id
            self.bot.sendMessage(self.owner, 'You have been set as owner')
        else:
            self.bot.sendMessage(self.owner, 'Wrong password')
            
    def reload(self):
        print('Reloading...')
        movies = self.scraper.get_new(self.last_movie_id, 1)
        text = '\n'.join([m['torrent_name'] for m in movies])
        if len(movies) > 0:
            self.last_movie_id = int(movies[0]['hd_id'])
            [self.send_movie(m) for m in movies]
    
    def send_movie(self, movie):
        # enhance movie info
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Download', callback_data=movie['hd_id'])],
               ])

        text = [
            f"*{movie['torrent_name'].replace('.torrent','').replace('.mkv','')}*",
            f"{movie['imdb_url']}",
            f"`{movie['resolution']}` - `{movie['size']} GB`",
            "",
            f"HDTorrent: [torrent]({movie['torrent_url'].replace(')','%29')}), [details]({movie['torrent_details_url']})",
        ]

        message = self.bot.sendMessage(self.owner, '\n'.join(text), reply_markup=keyboard, parse_mode='Markdown')
        self.movie_history[movie['hd_id']] = {'movie': movie, 'message':message}

if __name__ == '__main__':
    pass