n = int(input())

lcm_result = 1

for _ in range(n):
    num = int(input())
    denom = int(input())
    gcd_value = 1

    a, b = lcm_result, denom
    while b:
        a, b = b, a % b
    gcd_value = a

    lcm_result = (lcm_result * denom) // gcd_value

print(f"{lcm_result}/{gcd(lcm_result, lcm_result)}")