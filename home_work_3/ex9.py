def to_decimal(number_str, base):
    digits = "0123456789ABCDEF"
    decimal = 0
    for digit in number_str.upper():
        decimal = decimal * base + digits.index(digit)
    return decimal

def from_decimal(number, base):
    digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result if result else "0"

try:
    source_base = int(input("Исходная система (2-16): "))
    target_base = int(input("Целевая система (2-16): "))
    number = input("Число для преобразования: ")
    
    if not (2 <= source_base <= 16 and 2 <= target_base <= 16):
        print("Ошибка: система счисления должна быть от 2 до 16")
    else:
        decimal_value = to_decimal(number, source_base)
        result = from_decimal(decimal_value, target_base)
        print(f"Результат: {result}")
except ValueError:
    print("Ошибка ввода!")
    