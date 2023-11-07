initial_coins = int(input())

while initial_coins >= 8:
    divided_coins = initial_coins // 8
    excess_coins = initial_coins % 8
    remaining_coins = divided_coins
    initial_coins = remaining_coins
print(remaining_coins)
