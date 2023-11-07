password = input()
repeat = input()
if len(password) < 8:
    print('Короткий!')
elif password != repeat:
    print('Различаются')
else:
    print('OK')
