pile_one = int(input())
pile_two = int(input())

while True:
    pile_number = int(input())
    stones_taken = int(input())

    if pile_number == 1:
        pile_one -= stones_taken
    else:
        pile_two -= stones_taken

    print(pile_one, pile_two)

    if pile_one == 0 and pile_two == 0:
        break
