number = int(input())
power = 0

while number > 1 and number % 2 == 0:
    number //= 2
    power += 1

if number == 1:
    print(power)
else:
    print("НЕТ")