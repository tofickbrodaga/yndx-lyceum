n = int(input())

while n != 0:
    put = int(input())
    if put <= 3 and put > 0 and put <= n:
        n -= put
        print(n)
    else:
        print(n)