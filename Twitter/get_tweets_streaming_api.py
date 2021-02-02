import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_client import get_twitter_auth

class CustomListener(StreamListener):
    """Специальный прослушиватель потока StreamListener 
    для потокой передачи данных Twitter."""

    def __init__(self, fname):
        safe_fname = format_filename(fname)
        self.outfile = "stream_%s.jsonl" % safe_fname

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            sys.stderr.write("Ошибка on_data: {}\n".format(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        if status == 420:
            sys.stderr.write("Превышен лимит на частоту запросов\n".format(status))
            return False
        else:
            sys.stderr.write("Ошибка {}\n".format(status))
            return True

def format_filename(fname):
    """Конвертировать имя файла fname в безопасную строку для имени файла.

    Возвращает: строковое значение
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Конвертировать символ в '_', если он "недопустим".

    Возвращает: строковое значение
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

if __name__ == '__main__':
    query = sys.argv[1:]          # список аргументов командной строки
    query_fname = ' '.join(query) # строковое значение
    auth = get_twitter_auth()
    twitter_stream = Stream(auth, CustomListener(query_fname))
    twitter_stream.filter(track=query)
