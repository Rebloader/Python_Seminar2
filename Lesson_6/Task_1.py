# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import datetime
import calendar


def check_date(date: str) -> bool:
    format = '%d.%m.%Y'

    try:
        date = datetime.datetime.strptime(date, format)
        print(date)
        return True
    except:
        return False


def check_year(year: int) -> bool:
    return calendar.isleap(year)


def main():
    while True:
        action = input('Выберите действие:\n '
                       '1 - проверить дату \n '
                       '2 - проверить год \n '
                       '3 - выйти \n')
        if action not in ("1", "2", "3"):
            print("Неверный ввод")
            continue

        match action:
            case "1":
                date_to_check = input("Input date for check (dd.mm.yyyy): ")
                if check_date(date_to_check):
                    print(f"{date_to_check} is correct date")
                else:
                    print(f'{date_to_check} is incorrect')
            case "2":
                year_to_check = input("Input year for check: ")
                try:
                    year_to_check = int(year_to_check)
                    if check_year(year_to_check):
                        print(f'Year {year_to_check} is leap')
                    else:
                        print(f'Year {year_to_check} is not leap')
                except ValueError:
                    print('Input correct year!')
            case "3":
                break


if __name__ == '__main__':
    main()
