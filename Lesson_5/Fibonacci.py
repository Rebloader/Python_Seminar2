# Создайте функцию генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def main():
    generate_fib = fibonacci()
    for _ in range(13):
        print(next(generate_fib))


if __name__ == '__main__':
    main()