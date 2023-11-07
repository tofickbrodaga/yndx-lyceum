words = []
while True:
    word = input().lower()
    if word == 'СТОП':
        break
    words.append(word)

count = 0
idx = 0
idxitem = []
for item in words:
    if 'кот' in item:
        count += 1
        idx = words.index(item) + 1
        idxitem.append(idx)

idxitem.sort()
if count > 0:
    print(idxitem[0])
else:
    print(-1)