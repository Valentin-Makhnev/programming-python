text = input("Введите предложение: ").lower()
stats = {}
for char in text:
    if char != ' ':
        stats[char] = stats.get(char, 0) + 1

for char, count in stats.items():
    print(f"{char}={count}")
    