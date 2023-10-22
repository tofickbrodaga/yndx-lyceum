question_one = str(input('Любите ли вы котиков? ^..^: '))
question_two = str(input('Любите ли вы программировать? ^..^: '))

question_one = question_one.lower()
question_two = question_two.lower()

if question_one == 'да' and question_two == 'нет':
    print('Вы котик не программист ^..^')
elif question_one == 'нет' and question_two == 'да':
    print('Вы просто программист :)')
elif question_one == 'да' and question_two == 'да':
    print('Вы котик и программист ^..^')
else:
    print('Вы не котик и не программист ^..^')