num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)

middle = (num1 + num2 + num3) - minimum - maximum

print(f"Числа в порядке возрастания: {minimum}, {middle}, {maximum}")
