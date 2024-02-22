# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction


def str_to_fractions(str_fraction):
    divisible, divider = map(int, str_fraction.split('/'))
    return Fraction(divisible, divider)


def sum_fraction(fraction_1, fraction_2):
    return fraction_1 + fraction_2


def power_fractions(fraction_1, fraction_2):
    return fraction_1 * fraction_2


def main():
    fraction_1 = str_to_fractions(input('введите первую дробь: '))
    fraction_2 = str_to_fractions(input('введите вторую дробь: '))
    print('сумма: ', sum_fraction(fraction_1, fraction_2))
    print('произведение:  ', power_fractions(fraction_1, fraction_2))


if __name__ == '__main__':
    main()
