# Напишите функцию для транспонирования матрицы


def transpose_matrix(matrix):
    rows_matrix = len(matrix)
    columns_matrix = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows_matrix)] for _ in range(columns_matrix)]

    for i in range(rows_matrix):
        for j in range(columns_matrix):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    transposed = transpose_matrix(matrix)
    for row in transposed:
        print(row)


if __name__ == '__main__':
    main()
