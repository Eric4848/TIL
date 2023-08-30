import sys

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]   # 연결된 친구관계를 저장할 리스트
is_friend = [False] * N   # 이미 연결한 사람을 확인할 리스트
answer = [0]   # 정답을 0으로 초기화
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)


def dfs(i, d):
    if d == 4:   # dfs를 4번진행 -> 5명이 연결되면
        answer[0] = 1   # 정답을 1로 수정한다
        return

    if not is_friend[i]:   # 연결되지 않은 사람이면
        is_friend[i] = True   # 연결하고
        for nxt in matrix[i]:   # 그 사람과 연결된 사람들 중
            if not is_friend[nxt]:   # 연결되지 않은 사람이라면
                dfs(nxt, d+1)   # 다음 dfs로 넘겨준다
        is_friend[i] = False   # 연결을 풀어준다


for i in range(N):   # 모든 인원을
    dfs(i, 0)   # 시작 인원으로 설정하여 반복한다
    if answer[0] == 1:   # 가능하다면
        break   # 반복을 중단한다
print(answer[0])
