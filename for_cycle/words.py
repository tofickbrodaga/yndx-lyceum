delimiter = input()
words = []

for _ in range(3):
    word = input()
    words.append(word)

result = delimiter.join(words)
print(result)
