from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

numbers = list(map(int, input("Введите числа через пробел: ").split()))
if numbers:
    nod = reduce(gcd, numbers)
    nok = reduce(lcm, numbers)
    print(f"НОД: {nod}")
    print(f"НОК: {nok}")
