def solution(m, n, puddles):
    matrix = [[-1] * m for _ in range(n)]

    for c, r in puddles:
        matrix[r-1][c-1] = 0

    num = 1
    for i in range(m):
        if matrix[0][i] == 0:
            num = 0
        matrix[0][i] = num

    num = 1
    for i in range(n):
        if matrix[i][0] == 0:
            num = 0
        matrix[i][0] = num

    for r in range(1, n):
        for c in range(1, m):
            if matrix[r][c] != 0:
                matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]

    return matrix[n-1][m-1] % 1000000007


print(solution(4, 3, [[2, 2]]))


# def solution(m, n, puddles):
#     answer = 0
#     matrix = [[0] * m for _ in range(n)]
#     matrix_len = [n, m]
#     for r, c in puddles:
#         matrix[c - 1][r - 1] = 1
#     walked = float('INF')
#
#     def walk(now, move):
#         nonlocal walked, answer
#
#         if move > walked:
#             return
#
#         if matrix[now[0]][now[1]] == 1:
#             return
#
#         if now == [n - 1, m - 1]:
#             if move < walked:
#                 walked = move
#                 answer = 1
#             elif move == walked:
#                 answer += 1
#             return
#
#         for i in range(2):
#             if now[i] == matrix_len[i]-1:
#                 continue
#             now[i] += 1
#             walk(now, move+1)
#             now[i] -= 1
#     walk([0, 0], 0)
#     answer = answer % 1000000007
#     return answer
#