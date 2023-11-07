low = 1
high = 1000
attempts = 0

while low <= high and attempts < 10:
    mid = (low + high) // 2
    print(mid)
    response = input()

    if response == '>':
        low = mid + 1
    elif response == '<':
        high = mid - 1
    elif response == '=':
        print('Угадал!')
        break

    attempts += 1

if attempts == 10:
    print('Не удалось угадать за 10 попыток.')
