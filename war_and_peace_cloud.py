import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud

if __name__ == '__main__':
    fname = input('Введите имя файла: ', )
    all_posts = []

    with open(fname, 'r', encoding='cp1251') as f:
        data = f.read()

    with open('russian_stopwords.txt', 'r', encoding='utf-8') as f:
        russian_stopwords = f.read().splitlines()

    stop_list = stopwords.words('russian') + russian_stopwords
    wordcloud = WordCloud(stopwords=stop_list).generate(data)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('Wordcloud {}.png'.format(fname[:fname.find('.')]))