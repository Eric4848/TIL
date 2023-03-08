matrix = [[0 for _ in range(19)] for _ in range(19)]
n = int(input())
for _ in range(n):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1
for i in range(19):
    print(*matrix[i])
