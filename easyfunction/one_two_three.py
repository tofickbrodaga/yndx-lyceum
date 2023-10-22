a, b, c = int(input()), int(input()), int(input())

lst = [a, b, c]

lst = sorted(lst, reverse=True)
for i in lst:
    print(i)