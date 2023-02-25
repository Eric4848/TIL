matrix = [list(map(int, input().split())) for _ in range(10)]

now = [1, 1]

while matrix[now[0]][now[1]] != 2:
    if now[0] == 9 or now[1] == 9:
        break

    matrix[now[0]][now[1]] = 9
    if matrix[now[0]][now[1]+1] != 1:
        now[1] += 1

    elif matrix[now[0]+1][now[1]] != 1:
        now[0] += 1

    elif matrix[now[0]][now[1]+1] == 1 and matrix[now[0]+1][now[1]] == 1:
        break
matrix[now[0]][now[1]] = 9
for i in range(10):
    print(*matrix[i])
