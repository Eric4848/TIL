N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answers = []


def dfs(s):
    for i in range(N):
        if graph[s][i] == 1 and visits[i] == 0:
            visits[i] = 1
            dfs(i)


for j in range(N):
    visits = [0 for _ in range(N)]
    dfs(j)
    answers.append(visits)

for answer in answers:
    print(*answer)
