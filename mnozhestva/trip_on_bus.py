auto_numb = set()
auto_numb_t = set()

while True:
    number = input()
    if number != '':
        auto_numb.add(number)
    else:
        break

while True:
    number = input()
    if number != '':
        auto_numb_t.add(number)
    else:
        break

count = 0

for i in auto_numb:
    if i in auto_numb_t:
        print(i)
        count += 1
if count == 0:
    print('EMPTY')