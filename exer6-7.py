def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word
user_words = input('Введите строку из нескольких слов ')
for word in user_words.split(' '):
    print(f'{int_func(word)}', end=' ')

