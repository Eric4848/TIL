row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]

for i in range(1, col):
    matrix[0][i] += matrix[0][i-1]
for i in range(1, row):
    matrix[i][0] += matrix[i-1][0]

for r in range(1, row):
    for c in range(1, col):
        matrix[r][c] += max(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])

print(matrix[row-1][col-1])


# row, col = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(row)]
# answer = [0]
#
#
# def dfs(r, c, summary):
#     summary += matrix[r][c]
#
#     if r == row - 1 and c == col - 1:
#         if summary > answer[0]:
#             answer.pop()
#             answer.append(summary)
#             return
#
#     if r < row - 1:
#         dfs(r + 1, c, summary)
#
#     if c < col - 1:
#         dfs(r, c + 1, summary)
#
#     if r < row - 1 and c < col - 1:
#         dfs(r + 1, c + 1, summary)
#
#
# dfs(0, 0, 0)
# print(answer[0])
