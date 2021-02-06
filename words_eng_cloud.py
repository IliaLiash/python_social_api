import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud

if __name__ == '__main__':
    fname = input('Input file name: ', )
    all_posts = []

    with open(fname, 'r', encoding='utf-8') as f:
        data = f.read()

    stop_list = stopwords.words('english')
    wordcloud = WordCloud(stopwords=stop_list).generate(data)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('wordcloud_{}.png'.format(fname[:fname.find('.')]))