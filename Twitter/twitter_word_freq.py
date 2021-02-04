import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import nltk
import matplotlib.pyplot as plt
nltk.data.path.append('D:\\nltk_data')


def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
    """Обработать текст твита:
    - Перевести литеры в нижний регистр
    - Лексемизировать
    - Удалить стоп-слова
    - Удалить цифры

    Возвращает: список строковых значений
    """
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()]

if __name__ == '__main__':
    tweet_tokenizer = TweetTokenizer()
    punct = list(string.punctuation)
    stopword_list = stopwords.words('russian') + stopwords.words('english') + punct + ['…', '«', '»', '—', 'это', 'rt']

    fname = input('Input file name: ', )
    tf = Counter()
    with open(fname, 'r') as f:
        for line in f:
            tweet = json.loads(line)    #Отдельно загружаем каждую строку
            tokens = process(text=tweet.get('text', ''),
                             tokenizer=tweet_tokenizer,
                             stopwords=stopword_list)
            tf.update(tokens)
        for tag, count in tf.most_common(30):
            print("{}: {}".format(tag, count))

    y = [count for tag, count in tf.most_common(100)]
    x = range(1, len(y) + 1)

    plt.bar(x, y)
    plt.title('Частота слов в твитах')
    plt.ylabel('Частота')
    plt.show()
