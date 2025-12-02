class1 = list(range(160, 177, 2))
class2 = list(range(162, 181, 3))

all_students = class1 + class2

all_students.sort()

print(f"Отсортированный список учеников: {all_students}")
