from mpmath import mp

n = int(input())
mp.dps = 15  # Количество знаков после запятой
sum_of_inverse_squares = mp.mpf(0)

for k in range(1, n + 1):
    sum_of_inverse_squares += 1 / (k * k)

pi = mp.pi
result = pi / sum_of_inverse_squares
print(f"{result}")