n = int(input())
approximation = 0

for i in range(n):
    term = (-1) ** i / (2 * i + 1)
    approximation += term

pi_approximation = 4 * approximation
print(pi_approximation)
