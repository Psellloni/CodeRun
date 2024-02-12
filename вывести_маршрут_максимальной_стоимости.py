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
                    matrix[i][j] += max(matrix[i][j - 1], matrix[i - 1][j])
                else:
                    matrix[i][j] += matrix[i - 1][j]

    moves = []
    n -= 1
    m -= 1

    while n != 0 or m != 0:
        if n == 0:
            moves = ['R'] * (m) + moves
            break

        elif m == 0:
            moves = ['D'] * (n) + moves
            break

        elif matrix[n-1][m] > matrix[n][m-1]:
            moves.insert(0, 'D')
            n -= 1

        else:
            moves.insert(0, 'R')
            m -= 1



    print(matrix[-1][-1])
    print(' '.join(moves))


if __name__ == '__main__':
    main()