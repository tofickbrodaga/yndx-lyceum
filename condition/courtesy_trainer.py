print('Назовите себя, пожалуйста!')
name = str(input())
print('Введите текст.')
text = str(input())
print('Повторите текст.')
text_repeat = str(input())
if text == text_repeat:
    print(f'{name}, введено верно!')
else:
    print(f'{name}, пока не получилось, попробуйте снова!')