first_list = []
for i in range(1, 4):
    num = int(input(f"Введите {i}-е число для первого списка: "))
    first_list.append(num)

second_list = []
for i in range(1, 8):
    num = int(input(f"Введите {i}-е число для второго списка: "))
    second_list.append(num)


print(f"\nПервый список: {first_list}")
print(f"Второй список: {second_list}")

first_list.extend(second_list)

first_list = list(set(first_list))

print(f"Новый первый список с уникальными элементами: {first_list}")
