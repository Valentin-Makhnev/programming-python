def grade_converter():
    print("Конвертер оценок")
    print("=" * 40)
    
    while True:
        user_input = input("Введите оценку (Enter - выход): ").strip()
        if user_input == "":
            print("Выход из программы.")
            break
        
        try:
            num = int(user_input)
            
            if 0 <= num <= 100:
                if 91 <= num <= 100:
                    print(f"{num} баллов -> Отлично (5, A)")
                elif 84 <= num <= 90:
                    print(f"{num} баллов -> Очень хорошо (4, B)")
                elif 74 <= num <= 83:
                    print(f"{num} баллов -> Хорошо (4, C)")
                elif 68 <= num <= 73:
                    print(f"{num} баллов -> Удовлетворительно (3, D)")
                elif 61 <= num <= 67:
                    print(f"{num} баллов -> Посредственно (3, E)")
                elif 0 <= num <= 60:
                    print(f"{num} баллов -> Неудовлетворительно (2, P)")
            
            elif user_input in ['2', '3', '4', '5']:
                if user_input == '5':
                    print("5 -> Отлично (A, 91-100 баллов)")
                elif user_input == '4':
                    print("4 -> Очень хорошо (B, 84-90) или Хорошо (C, 74-83)")
                elif user_input == '3':
                    print("3 -> Удовлетворительно (D, 68-73) или Посредственно (E, 61-67)")
                elif user_input == '2':
                    print("2 -> Неудовлетворительно (P, 0-60 баллов)")
            else:
                print(f"Число {num} не соответствует системе оценок")
                
        except ValueError:
            grade = user_input.upper()
            if grade == 'A':
                print("A -> Отлично (5, 91-100 баллов)")
            elif grade == 'B':
                print("B -> Очень хорошо (4, 84-90 баллов)")
            elif grade == 'C':
                print("C -> Хорошо (4, 74-83 баллов)")
            elif grade == 'D':
                print("D -> Удовлетворительно (3, 68-73 баллов)")
            elif grade == 'E':
                print("E -> Посредственно (3, 61-67 баллов)")
            elif grade == 'P':
                print("P -> Неудовлетворительно (2, 0-60 баллов)")
            else:
                print(f"'{user_input}' - недопустимая оценка. Используйте: A, B, C, D, E, P или числа 0-100")

grade_converter()
