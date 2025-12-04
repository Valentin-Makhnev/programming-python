date_str = input("Введите дату (ДД.ММ.ГГГГ): ")
day, month, year = map(int, date_str.split('.'))

if day * month == year % 100:
    print("Магическая дата")
else:
    print("Не магическая дата")
