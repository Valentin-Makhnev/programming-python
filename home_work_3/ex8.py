print("Загадайте число от 1 до 100")
low, high = 1, 100
attempts = 0

while low <= high and attempts < 7:
    mid = (low + high) // 2
    answer = int(input(f"Твое число равно(1), больше(2) или меньше(3), чем {mid}? "))
    attempts += 1
    
    if answer == 1:
        print(f"Угадал за {attempts} попыток!")
        break
    elif answer == 2:
        low = mid + 1
    elif answer == 3:
        high = mid - 1
else:
    print("Что-то пошло не так...")
    