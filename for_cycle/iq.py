n = int(input())
iq_values = [int(input()) for _ in range(n)]

average_iq = 0
for i, iq in enumerate(iq_values):
    if i == 0:
        print('0')
        average_iq = iq
    else:
        if iq > average_iq:
            print('>')
        elif iq < average_iq:
            print('<')
        else:
            print('0')
    average_iq = (average_iq * i + iq) / (i + 1)