# Находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
# Находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы)
# Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.
# Например, было введено число 167. Строим сумму старших разрядов – 1 + 6 = 7, 
# строим сумму младших разрядов – 6 + 7 = 13. 
# Полученные две суммы 7 и 13 записываем друг за другом в порядке не возрастания, те 137. Искомое число – 137.

digit = int(input())

one = digit // 100
two = digit // 10 - 10
three = digit % 10

res = [one + two, two + three]
res = sorted(res, reverse=True)
res = str(res[0]) + str(res[1])

print(int(res))

a = int(input())
b = a % 10 #1
c = a % 100 //10 #10
d = a // 100 #100
sum1 = d + c
sum2 = b + c
if sum1 > sum2:
   print(sum1, sum2)
else:
   print(sum2, sum1)