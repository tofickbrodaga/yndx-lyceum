print('Как у вас настроение?')
word = input()
if word.startswith('хорош') or word.startswith('прекрасн'):
    print('Отлично, у меня тоже всё хорошо :)')
elif 'плох' in word:
    print('Ничего, скоро всё наладится')
elif 'не' in word:
    print('Извините, но я вас не понимаю')
elif '?' in word:
    print('Извините, но я вас не понимаю')
else:
    print('Извините, но я вас не понимаю')