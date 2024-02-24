# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

RICH = 5_000_000
AMOUNT_VALUE = 50
transactions = []


def add_money(balance, count):
    while True:
        try:
            summ = int(input(f"Введите сумму пополнения, кратную {AMOUNT_VALUE}: "))
        except:
            ex = input("Хотите выйти в меню? (yes/no)\n")
            if ex.lower() == 'y':
                return balance, count
            else:
                continue

        if summ % AMOUNT_VALUE == 0:
            balance += summ
            count += 1
            if count % 3 == 0:
                balance *= 1.03
            transactions.append(('пополнение', summ))
            return balance, count
        else:
            print(f'Сумма должна быть кратна {AMOUNT_VALUE}')


def get_money(balance, count):
    if balance > RICH:
        balance *= 0.9

    while True:
        try:
            summ = int(input(f"Введите сумму снятия, кратную {AMOUNT_VALUE}: "))
        except:
            ex = input("Хотите выйти в меню? (yes/no)\n")
            if ex.lower() == 'yes':
                return balance, count
            else:
                continue

        if summ % AMOUNT_VALUE == 0:
            perc = min(max(summ * 0.015, 30), 600)
            total_summ = summ + perc
            if total_summ > balance:
                print("Недостаточно средств!")
            else:
                balance -= total_summ
                count += 1
                if count % 3 == 0:
                    balance *= 1.03
                transactions.append(('снятие', summ))
                return balance, count
        else:
            print(f'Сумма должна быть кратна {AMOUNT_VALUE}')


def main():
    balance = 0
    count = 0
    print('Добро пожаловать в банкомат!')

    while True:
        action = input('Выберите действие:\n 1 - пополнить \n 2 - снять \n 3 - список операций \n 4 - выйти\n')
        if action not in ("1", "2", "3", "4"):
            print("Неверный ввод")
            continue

        match action:
            case "1":
                balance, count = add_money(balance, count)
                print(f"Ваш баланс: {balance}")
            case "2":
                balance, count = get_money(balance, count)
                print(f"Ваш баланс: {balance}")
            case "3":
                for item in transactions:
                    print(item)
            case "4":
                print(f"Ваш баланс: {balance}")
                print("До свидания!")
                break


if __name__ == "__main__":
    main()
