from gensim.summarization import summarize

with open('palace.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    summary = summarize(content, split=True)
    for i, sentence in enumerate(summary):
        print(f'{i+1}) {sentence}')

'''
summarize() - ранжирует предложения согласно их важности и выбирает самые характерные,
чтобы сгенерировать итоговое краткое изложение. Результат - примерно 25% от текста.
'''