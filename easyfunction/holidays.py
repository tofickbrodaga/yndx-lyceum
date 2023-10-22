city_one, city_two = input(), input()

OK_test1 = 'Тула'
OK_test2 = 'Пенза'

if (city_one == OK_test1 and city_two == OK_test2) or \
        (city_one == OK_test1 and city_two != OK_test2) or \
            (city_one != OK_test1 and city_two == OK_test2):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')