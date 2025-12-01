import math

operand1 = int(input("Введите первый операнд: "))
operand2 = int(input("Введите второй операнд: "))

print("\n=== Арифметические операции ===")

result = operand1 + operand2
print(f"{operand1} + {operand2} = {result}")

result = operand1 - operand2
print(f"{operand1} - {operand2} = {result}")

result = operand1 * operand2
print(f"{operand1} * {operand2} = {result}")

if operand2 != 0:
    result = operand1 / operand2
    if isinstance(result, float):
        result = round(result, 2)
    print(f"{operand1} / {operand2} = {result}")
else:
    print(f"{operand1} / {operand2} = Ошибка: деление на ноль!")

if operand2 != 0:
    result = operand1 // operand2
    print(f"{operand1} // {operand2} = {result}")
else:
    print(f"{operand1} // {operand2} = Ошибка: деление на ноль!")

if operand2 != 0:
    result = operand1 % operand2
    print(f"{operand1} % {operand2} = {result}")
else:
    print(f"{operand1} % {operand2} = Ошибка: деление на ноль!")

result = operand1 ** operand2
if isinstance(result, float):
    result = round(result, 2)
print(f"{operand1} ** {operand2} = {result}")

if operand1 > 0:
    result = math.log10(operand1)
    if isinstance(result, float):
        result = round(result, 2)
    print(f"log10({operand1}) = {result}")
else:
    print(f"log10({operand1}) = Ошибка: логарифм определен только для положительных чисел!")

if operand2 > 0:
    result = math.log10(operand2)
    if isinstance(result, float):
        result = round(result, 2)
    print(f"log10({operand2}) = {result}")
else:
    print(f"log10({operand2}) = Ошибка: логарифм определен только для положительных чисел!")

print("\n=== Операции сравнения ===")

result = operand1 < operand2
print(f"{operand1} < {operand2} = {result}")

result = operand1 <= operand2
print(f"{operand1} <= {operand2} = {result}")

result = operand1 > operand2
print(f"{operand1} > {operand2} = {result}")

result = operand1 >= operand2
print(f"{operand1} >= {operand2} = {result}")

result = operand1 != operand2
print(f"{operand1} != {operand2} = {result}")

result = operand1 == operand2
print(f"{operand1} == {operand2} = {result}")
