m = int(input())
n = int(input())

students_english = set()
students_germany = set()

while m > 0:
    last_name = input()
    students_english.add(last_name)
    m -= 1

while n > 0:
    last_name = input()
    students_germany.add(last_name)
    n -= 1

count = len(students_english ^ students_germany)
print(count if count > 0 else 'NO')
