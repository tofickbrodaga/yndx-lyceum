count_city = int(input())

cities = set()

while count_city > 0:
    city = input()
    cities.add(city)
    count_city -= 1

another_city = input()
if another_city not in cities:
    print('OK')
else:
    print('TRY ANOTHER')