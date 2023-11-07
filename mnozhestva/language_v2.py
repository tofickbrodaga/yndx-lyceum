M = int(input())
N = int(input())

english_students = set()
german_students = set()

for i in range(M):
    name = input()
    english_students.add(name)

for i in range(N):
    name = input()
    german_students.add(name)

only_one_language_students = (english_students.symmetric_difference(german_students))

if only_one_language_students:
    print(len(only_one_language_students))
else:
    print("NO")
