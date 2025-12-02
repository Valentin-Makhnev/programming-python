shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], 
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], 
        ['седло', 2700]]

detail_name = input("Название детали: ").strip().lower()

count = 0
total_cost = 0

for item, price in shop:
    if item == detail_name:
        count += 1
        total_cost += price

if count > 0:
    print(f"Кол-во деталей — {count}")
    print(f"Общая стоимость — {total_cost}")
else:
    print("Деталь не найдена")
    