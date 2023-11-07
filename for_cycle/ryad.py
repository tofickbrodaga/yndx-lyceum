n = int(input())
numbers = [int(input()) for _ in range(n)]

result = 0
for i in range(n):
    if i % 2 == 0:
        result += numbers[i]
    else:
        result -= numbers[i]

print(result)
