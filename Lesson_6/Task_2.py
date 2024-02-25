# Напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8
# можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них
# пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют
# друг друга верните истину, а если бьют - ложь.


def check_queen_placement(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == (y1 - y2):
                return False
    return True


def main():
    queens = []
    for _ in range(8):
        x, y = map(int, input('Input queens coords (int int): ').split())
        queens.append((x, y))

    if check_queen_placement(queens):
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()

