v = float(input("Введите скорость спортсмена (км/ч): "))
t = float(input("Введите время в пути (часов): "))

length = 123

distance = v * t

position = int(distance) % length

print(f"Спортсмен остановится на {position}-м километре")
