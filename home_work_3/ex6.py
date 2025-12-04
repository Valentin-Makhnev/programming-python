def split_numbers(*args):
    negative = sorted([x for x in args if x < 0], reverse=True)
    non_negative = sorted([x for x in args if x >= 0])
    return (negative, non_negative)

numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = split_numbers(*numbers)
print(f"Отрицательные: {result[0]}")
print(f"Неотрицательные: {result[1]}")
