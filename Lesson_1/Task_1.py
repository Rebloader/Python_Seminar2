def check_triangle(a, b, c):
    if a <= 0 and b <= 0 and c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def triangle_type(a, b, c):
    if a == b == c:
        return 'равносторонний'
    elif a == b or a == c or b == c:
        return 'равнобедренный'
    else:
        return 'разносторонний'


def main():
    a = int(input("Input first side of triangle: "))
    b = int(input("Input second side of triangle: "))
    c = int(input("Input third side of triangle: "))

    if check_triangle(a, b, c):
        print("Треугольник существует.")
        print("Тип треугольника: ", triangle_type(a, b, c))
    else:
        print("Такого треугольника не существует")


if __name__ == '__main__':
    main()
