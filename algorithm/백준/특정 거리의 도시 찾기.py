import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
moves = [-1] * (N+1)   # 이동횟수를 -1로 초기화
moves[X] = 0   # 시작지점의 이동횟수를 0으로 설정
matrix = [[] for _ in range(N + 1)]
answer = []   # 정답 리스트

for _ in range(M):
    s, e = map(int, input().split())
    matrix[s].append(e)

q = deque()
q.append(X)

while q:
    now = q.popleft()   # 현재 위치
    for nxt in matrix[now]:   # 현재 위치에서 갈 수 있는 곳들
        if moves[nxt] == -1:   # 가보지 않은 곳이면
            moves[nxt] = moves[now] + 1   # 현재 위치까지 이동횟수 + 1을 저장하고
            q.append(nxt)   # 큐에도 추가
            if moves[nxt] == K:   # 저장한 이동횟수가 목표 이동횟수와 같다면
                answer.append(nxt)   # 정답에 추가

if answer:   # 정답이 있으면
    answer.sort()   # 정렬하여
    for ans in answer:   # 각각 출력한다
        print(ans)
else:
    print(-1)
