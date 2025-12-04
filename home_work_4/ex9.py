class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)

def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))

def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег с счета 'account_from' на 'account_to'."""
    try:
        if account_from not in accounts:
            raise PaymentError(f"Счет {account_from} не найден")
        if account_to not in accounts:
            raise PaymentError(f"Счет {account_to} не найден")
        if accounts[account_from] < value:
            raise NoMoneyToWithdrawError(f"Недостаточно средств у {account_from}")
        
        # Сохраняем исходные значения для отката
        old_from = accounts[account_from]
        old_to = accounts[account_to]
        
        accounts[account_from] -= value
        accounts[account_to] += value
        
    except Exception as e:
        # Восстанавливаем исходные значения при ошибке
        accounts[account_from] = old_from
        accounts[account_to] = old_to
        raise PaymentError(f"Ошибка перевода: {str(e)}")

if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".format(**payment_info))
    
    try:
        payment_info["value"] = int(input("Сумма = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
    except (ValueError, NoMoneyToWithdrawError, PaymentError) as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    
    print_accounts(accounts)
    