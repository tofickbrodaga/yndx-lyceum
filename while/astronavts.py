heights = []

while True:
    height = input()
    
    if height == "!":
        break
    
    height = int(height)
    
    if 150 <= height <= 190:
        heights.append(height)

print(len(heights))
print(min(heights), max(heights))