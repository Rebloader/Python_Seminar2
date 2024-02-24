# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def args_to_dict(*args):
    names, salaries, percents = zip(*args)
    return {name: int(salary) * (float(percent) / 100)
            for name, salary, percent in zip(names, salaries, percents)}


def main():
    param_1 = ['John', 80000, '10.15']
    param_2 = ['Mary', 120000, '5.1']
    param_3 = ['Bob', 150000, '7.5']

    result_dict = args_to_dict(param_1, param_2, param_3)
    print(result_dict)


if __name__ == '__main__':
    main()

