N = int(input())
tables = []
answer = 0
for _ in range(N):
    tables.append(list(map(int, input().split())))

tables.sort(key=lambda x: x[0])
tables.sort(key=lambda x: x[1])
E = tables[0][1]
answer += 1

for i in range(1, N):
    if tables[i][0] >= E:
        answer += 1
        E = tables[i][1]

print(answer)
