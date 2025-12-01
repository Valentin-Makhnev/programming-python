team = input("Введите название футбольной команды: ")

print(f"{team} - чемпион!")

line = "-" * len(team)
print(line)

team_lower = team.lower()
print(f"Название в нижнем регистре: {team_lower}")

print(f"Длина наименования: {len(team)} символов")


has_p = "п" in team_lower
print(f"Есть ли буква 'п' в названии? {has_p}")

count_a = team_lower.count("а")
print(f"Буква 'а' встречается {count_a} раз(а)")
