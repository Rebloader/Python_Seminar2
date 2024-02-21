def check_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    num = int(input("Input number: "))
    if num <0 or num > 100000:
        print("число не входит в заданный диапазон")
    else:
        if check_number(num):
            print("число простое")
        else:
            print("число составное")


if __name__ == '__main__':
    main()
