h, w = map(int, input().split())
matrix = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())

dr = [0, 1]
dc = [1, 0]

for _ in range(n):
    l, d, x, y = map(int, input().split())
    now = [x-1, y-1]
    for _ in range(l):
        matrix[now[0]][now[1]] = 1
        now[0] += dr[d]
        now[1] += dc[d]
for i in range(h):
    print(*matrix[i])

