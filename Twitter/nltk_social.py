from nltk import word_tokenize, sent_tokenize
from nltk.tokenize import TweetTokenizer

text ='Фонд борьбы с коррупцией выпустил фильм о «дворце Путина» под Геленджиком, \
      построенном, как утверждается, минимум за 100 миллиардов рублей.'

words = word_tokenize(text)
sentences = sent_tokenize(text)
print(words)
print(sentences)

tokenizer = TweetTokenizer()
tweet = '@fbkinfo Наши новые точки сбора — станции метро «Сухаревская» и «Красные ворота».\
Подписывайтесь на телеграм-канал штаба Навального в Москве, там самая оперативная информация:\
http://t.me/teamnavalny_mos'

print(tokenizer.tokenize(tweet))
