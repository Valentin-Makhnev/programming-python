main_list = [1, 5, 3]
first_extra = [1, 5, 1, 5]
second_extra = [1, 3, 1, 5, 3, 3]

main_list.extend(first_extra)
count_5 = main_list.count(5)
print(f"Кол-во цифр 5 при первом объединении: {count_5}")

while 5 in main_list:
    main_list.remove(5)

main_list.extend(second_extra)
count_3 = main_list.count(3)
print(f"Кол-во цифр 3 при втором объединении: {count_3}")

print(f"Итоговый список: {main_list}")
