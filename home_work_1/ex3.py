import math

# Ввод данных
x = int(input("Введите x (целое число): "))
y = int(input("Введите y (целое число, не равное 0): "))
z = int(input("Введите z (целое число): "))

# Проверка на ноль в знаменателе
if y == 0:
    print("Ошибка: y не может быть равно 0 (деление на ноль под корнем)")
elif (7 - (z % y)) == 0:
    print("Ошибка: знаменатель (7 - z mod y) равен 0")
else:
    under_root = (x**5 + 7) / (6 * y)
    
    if under_root >= 0:
        cube_root = under_root ** (1/3)
    else:
        cube_root = -((-under_root) ** (1/3))
    
    denominator = 7 - (z % y)
    f = cube_root / denominator
    
    f = round(f, 3)
    

    print(f"Округленный результат: {f}")
