total_cost = 0

while True:
    price = float(input())
    
    if price < 0:
        break
    
    total_cost += price

if total_cost > 1000:
    discount = 0.05 * total_cost
    total_cost -= discount

print(total_cost)
