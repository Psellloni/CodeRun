def main():
    mas = list(map(int, input().split()))
    n, m = mas[0], mas[1]

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j != 0:
                matrix[i][j] += matrix[i][j - 1]
            elif i != 0:
                if j != 0:
                    matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j])
                else:
                    matrix[i][j] += matrix[i - 1][j]

    print(matrix[-1][-1])


if __name__ == '__main__':
    main()