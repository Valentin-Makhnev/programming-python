total = 0

while True:
    user_input = input("Введите число (Enter для выхода): ")
    
    if user_input == "":
        break
    
    try:
        number = float(user_input)
        total += number
        print(f"Текущая сумма: {total}")
    except ValueError:
        print("Ошибка: введите число!")

print(f"Итоговая сумма: {total}")
