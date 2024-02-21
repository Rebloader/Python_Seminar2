from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def find_number(number, input_number):
    if input_number < number:
        return 'меньше'
    if input_number > number:
        return 'больше'
    else:
        return 'угадали'


def main():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    # print(number)

    count = 0
    while count < 10:
        input_number = int(input("Input your number: "))
        print(find_number(number, input_number))
        if find_number(number, input_number) == 'угадали':
            break
        count += 1


if __name__ == '__main__':
    main()
