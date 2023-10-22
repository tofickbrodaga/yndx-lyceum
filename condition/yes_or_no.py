phrase_one, phrase_two = input(), input()

phrase_one = phrase_one.lower()
phrase_two = phrase_two.lower()

if phrase_one and phrase_two == 'да' or phrase_one and phrase_two == 'нет':
    print('ВЕРНО')
if phrase_one or phrase_two == '':
    print('НЕВЕРНО')
else: 
    print('НЕВЕРНО')