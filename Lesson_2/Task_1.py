# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def number_to_str_value(number):
    return hex(number)


def main():
    number = int(input('Input your number: '))
    print(number_to_str_value(number))
    if number_to_str_value(number) == hex(number):
        print("OK")
    else:
        print("Something wrong")


if __name__ == '__main__':
    main()