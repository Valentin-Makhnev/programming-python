n = int(input("Кол-во чисел: "))
sequence = []
for i in range(n):
    num = int(input(f"Число: "))
    sequence.append(num)

print(f"\nПоследовательность: {sequence}")

def is_symmetric(lst):
    return lst == lst[::-1]

if is_symmetric(sequence):
    print("Нужно приписать чисел: 0")
    print("Сами числа: []")
else:
    for i in range(n):
        sub_sequence = sequence[i:]
        if is_symmetric(sub_sequence):
            numbers_to_add = sequence[:i][::-1]
            count = len(numbers_to_add)
            
            print(f"Нужно приписать чисел: {count}")
            print(f"Сами числа: {numbers_to_add}")
            break
        