num2 = int(input("Введите двузначное число: "))
if 10 <= num2 <= 99:
    digit1_2 = num2 // 10
    digit2_2 = num2 % 10
    sum2 = digit1_2 + digit2_2
    prod2 = digit1_2 * digit2_2
    print(f"Двузначное число: {num2}")
    print(f"Сумма цифр: {sum2}")
    print(f"Произведение цифр: {prod2}")
else:
    print("Ошибка: введено не двузначное число\n")


num3 = int(input("Введите трехзначное число: "))
if 100 <= num3 <= 999:
    digit1_3 = num3 // 100
    digit2_3 = (num3 // 10) % 10
    digit3_3 = num3 % 10
    sum3 = digit1_3 + digit2_3 + digit3_3
    prod3 = digit1_3 * digit2_3 * digit3_3
    print(f"Трехзначное число: {num3}")
    print(f"Сумма цифр: {sum3}")
    print(f"Произведение цифр: {prod3}")
else:
    print("Ошибка: введено не трехзначное число")
    