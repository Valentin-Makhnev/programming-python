from collections import deque

n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек\n")

people = deque(range(1, n + 1))

while len(people) > 1:
    print(f"Текущий круг людей: {list(people)}")
    
    people.rotate(-(k - 1))
    
    out_person = people.popleft()
    print(f"Выбывает человек под номером {out_person}\n")

print(f"Остался человек под номером {people[0]}")
