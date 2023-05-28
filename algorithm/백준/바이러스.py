N = int(input())
M = int(input())

is_virus = [False] * (N+1)
is_virus[1] = True
matrix = [[] for _ in range(N+1)]
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
connect = matrix[1]

while connect:
    nxt = connect.pop()
    if not is_virus[nxt]:
        answer += 1
        connect += matrix[nxt]
        is_virus[nxt] = True

print(answer)
