N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]


def search(L):
    start_s = matrix[0][0]
    is_same_s = True
    answer = [0, 0, 0]
    for i in range(L):
        for j in range(L):
            if matrix[i][j] != start_s:
                is_same_s = False

    def dfs(r, c, l):
        nonlocal answer
        start_d = matrix[r][c]
        is_same_d = True
        for m in range(r, r + l):
            for n in range(c, c + l):
                if matrix[m][n] != start_d:
                    is_same_d = False

        if is_same_d:
            if start_d == -1:
                answer[0] += 1
            elif start_d == 0:
                answer[1] += 1
            else:
                answer[2] += 1
        else:
            length = int(l / 3)
            dfs(r + 0, c + 0, length)
            dfs(r + 0, c + length, length)
            dfs(r + 0, c + 2 * length, length)
            dfs(r + length, c + 0, length)
            dfs(r + length, c + length, length)
            dfs(r + length, c + 2 * length, length)
            dfs(r + 2 * length, c + 0, length)
            dfs(r + 2 * length, c + length, length)
            dfs(r + 2 * length, c + 2 * length, length)

    if not is_same_s:
        Length = int(L / 3)
        dfs(0, 0, Length)
        dfs(0, Length, Length)
        dfs(0, 2 * Length, Length)
        dfs(Length, 0, Length)
        dfs(Length, Length, Length)
        dfs(Length, 2 * Length, Length)
        dfs(2 * Length, 0, Length)
        dfs(2 * Length, Length, Length)
        dfs(2 * Length, 2 * Length, Length)
    else:
        if start_s == -1:
            answer[0] += 1
        elif start_s == 0:
            answer[1] += 1
        else:
            answer[2] += 1

    print(answer[0])
    print(answer[1])
    print(answer[2])


search(N)
