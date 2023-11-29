# 실패 - 연결 5개만 찾는 방식 - 최소가 아니다
N = int(input())
M = int(input())
computers = [False for _ in range(N+1)]
answer = [0]
lines = [list(map(int, input().split())) for _ in range(M)]
is_used = [False for _ in range(M)]

for i in range(M):
    answer[0] += lines[i][2]


def search(i, cost):
    if answer[0] < cost:
        return
    if sum(computers) == N:
        if cost < answer[0]:
            answer[0] = cost
            print(is_used)
            return

    a, b, c = lines[i]

    if computers[a] and not computers[b]:
        for j in range(M):
            if not is_used[j]:
                is_used[j] = True
                computers[b] = True
                search(j, cost+c)
                is_used[j] = False
                computers[b] = False

    if computers[b] and not computers[a]:
        for j in range(M):
            if not is_used[j]:
                is_used[j] = True
                computers[a] = True
                search(j, cost+c)
                is_used[j] = False
                computers[a] = False


for i in range(M):
    a, b, c = lines[i]
    is_used[i] = True
    computers[a] = True
    computers[b] = True
    search(0, c)
    is_used[i] = False
    computers[a] = False
    computers[b] = False
print(answer[0])
