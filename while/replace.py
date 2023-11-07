numb = int(input("Введите целое число: "))
digit = numb % 10
numb_two = digit
numb = numb // 10
 
while numb > 0:
    digit = numb % 10
    numb = numb // 10
    numb_two = numb_two * 10
    numb_two = numb_two + digit

print('"Обратное" ему число:', numb)