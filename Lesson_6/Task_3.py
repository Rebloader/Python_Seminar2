# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint


def check_queen_placement(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == (y1 - y2):
                return False
    return True


def main():
    count = 0
    while count < 4:
        queens = [(randint(1, 8), randint(1, 8)) for _ in range(8)]
        # print(queens)
        if check_queen_placement(queens):
            print(f'True coords: {queens}')
            count += 1


if __name__ == '__main__':
    main()
