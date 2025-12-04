n = int(input("Сколько предложений? "))
count = 0
for _ in range(n):
    sentence = input()
    if any(char.isdigit() for char in sentence):
        count += 1
print(f"Предложений с цифрами: {count}")
