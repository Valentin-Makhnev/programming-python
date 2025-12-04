text = input("Введите строку: ").lower()
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-i-1]:
        is_palindrome = False
        break
print("Это палиндром" if is_palindrome else "Это не палиндром")
