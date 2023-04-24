n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]


def start(sr, sc, slength):
    answer = ''

    def check(r, c, length):
        num = matrix[r][c]
        match = 1
        nonlocal answer
        for i in range(r, r + length):
            for j in range(c, c + length):
                if matrix[i][j] != num:
                    match = 0

        if match == 1:
            answer += str(num)
        else:
            answer += '('
            new_length = int(length / 2)

            check(r, c, new_length)
            check(r, c + new_length, new_length)
            check(r + new_length, c, new_length)
            check(r + new_length, c + new_length, new_length)

            answer += ')'

    check(sr, sc, slength)
    print(answer)


start(0, 0, n)
