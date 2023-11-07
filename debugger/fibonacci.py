n = int(input())

a = 1
b = a + 1

while n > 0:
    print(a+b)
    a += 1
    b += 1
    n -= 1

money = float(input())
if money <= 10000:
    money *= 1.1
elif money <= 100000:
    money *= 1.2
else:
money *= 1.3
print('Вы получаете', money, '₽, поздравляем!')