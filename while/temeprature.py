total_temperature = 0
count = 0

while True:
    temperature = float(input())
    
    if temperature < -300:
        break
    
    total_temperature += temperature
    count += 1

average_temperature = total_temperature / count
print(average_temperature)