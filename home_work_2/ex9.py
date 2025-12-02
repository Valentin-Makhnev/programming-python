n = int(input("Кол-во друзей: "))
k = int(input("Долговых расписок: "))

balances = [0] * (n + 1)

for i in range(1, k + 1):
    print(f"\n{i}-я расписка")
    debtor = int(input("Кому: "))
    creditor = int(input("От кого: "))
    amount = int(input("Сколько: "))
    
    balances[debtor] -= amount
    balances[creditor] += amount

print("\nБаланс друзей:")
for i in range(1, n + 1):
    print(f"{i}: {balances[i]}")
