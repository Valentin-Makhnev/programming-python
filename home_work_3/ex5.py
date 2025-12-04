def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    for char in text:
        if 'а' <= char <= 'я':
            base = ord('а')
            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 32 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 32 + base)
            result.append(new_char)
        elif 'А' <= char <= 'Я':
            base = ord('А')
            if mode == 'encrypt':
                new_char = chr((ord(char) - base + shift) % 32 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 32 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
encrypted = caesar_cipher(text, shift, 'encrypt')
print(f"Зашифровано: {encrypted}")
decrypted = caesar_cipher(encrypted, shift, 'decrypt')
print(f"Расшифровано: {decrypted}")
