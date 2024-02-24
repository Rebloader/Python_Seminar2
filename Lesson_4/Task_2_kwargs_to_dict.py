# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def args_to_dict(**kwargs):
    return {value: key for key, value in kwargs.items()}


def main():
    args = args_to_dict(param_1=1, param_2=2, param_3=3)
    print(args)


if __name__ == '__main__':
    main()
   