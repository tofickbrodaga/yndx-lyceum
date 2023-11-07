count = int(input())
phrases = []
while count > 0:
    phrase = str(input()).lower()
    count -= 1
    phrases.append(phrase)

counter = 0
for item in phrases:
    if 'кот' in item:
        counter += 1

if counter > 0:
    print('МЯУ')
else:
    print('НЕТ')