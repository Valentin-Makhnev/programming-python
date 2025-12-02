n = int(input("Кол-во коньков: "))
skates = []
for i in range(1, n + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)


k = int(input("Кол-во людей: "))
people = []
for i in range(1, k + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    people.append(size)

skates.sort()
people.sort()

skates_index = 0
people_index = 0
count = 0

while skates_index < len(skates) and people_index < len(people):
    if skates[skates_index] >= people[people_index]:
        count += 1
        skates_index += 1
        people_index += 1
    else:
        skates_index += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count}")
