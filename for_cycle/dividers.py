results = []
for i in range(17):
    d = int(input())
    if d == 0:
        results.append("ДА")
    elif i % d == 0:
        results.append("ДА")
    else:
        results.append("НЕТ")

for result in results:
    print(result)
