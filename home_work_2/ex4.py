guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    
    action = input("Гость пришёл или ушёл? ").strip().lower()
    
    if action == "пора спать":
        break
    
    name = input("Имя гостя: ").strip()
    
    if action == "пришёл" or action == "пришел":
        if len(guests) < 6:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    
    elif action == "ушёл" or action == "ушел":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")
        else:
            print(f"Гость с именем {name} не найден на вечеринке.")
    
    else:
        print("Пожалуйста, введите 'пришёл' или 'ушёл'")

print("\nВечеринка закончилась, все легли спать.")
