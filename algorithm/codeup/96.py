matrix = []
for _ in range(19):
    matrix.append(list(map(int, input().split())))

n = int(input())
for _ in range(n):
    c, r = map(int, input().split())
    for j in range(19):
        if matrix[r-1][j] == 0:
            matrix[r-1][j] = 1
        else:
            matrix[r-1][j] = 0
        if matrix[j][c-1] == 0:
            matrix[j][c-1] = 1
        else:
            matrix[j][c-1] = 0

for i in range(19):
    print(*matrix[i])
