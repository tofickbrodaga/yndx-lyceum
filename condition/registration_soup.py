login = str(input())
mail = str(input())

if '@' not in login and '@' in mail:
    print('OK')
elif '@' in login and '@' in mail:
    print('Некорректный логин')
elif '@' in login and '@' not in mail:
    print('Некорректный логин')
elif '@' not in login and '@' not in mail:
    print('Некорректный адрес')