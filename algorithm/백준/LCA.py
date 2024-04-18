# Pypy 제출
import sys
from collections import deque


# 노드의 깊이와 상위노드를 설정하는 함수
def bfs(s):
    q = deque([s])   # 시작 지점
    while q:
        now = q.popleft()   # 현재 위치
        is_visit[now] = True   # 계산 처리
        for nxt in graph[now]:   # 이어져있는 다음 노드들
            if is_visit[nxt]:   # 이미 계산한 노드면
                continue   # 넘어간다
            d[nxt] = d[now]+1   # 깊이를 현재 깊이 + 1로 설정
            parents[nxt] = now   # 다음 노드의 부모노드를 현재로 설정
            q.append(nxt)   # 다음 노드를 큐에 추가


# 최소 공통 조상을 구하는 함수
def lca(a, b):
    while d[a] != d[b]:   # 두 노드의 깊이가 다르면
        # 깊이가 깊은쪽을 위로 올려준다(시작 노드부터의 거리가 같아야 하기 때문)
        if d[a] > d[b]:
            a = parents[a]
        else:
            b = parents[b]
    # 두 노드가 다르면 하나씩 위로 올려준다
    while a != b:
        a = parents[a]
        b = parents[b]

    return a   # 노드 반환


input = sys.stdin.readline
N = int(input())
parents = [i for i in range(N+1)]   # 부모노드 초기화
d = [0 for _ in range(N+1)]   # 깊이를 0으로 초기화
is_visit = [False for _ in range(N+1)]   # 방문하여 계산한지를 초기화
graph = [[] for _ in range(N+1)]   # 간선을 담을 리스트

# 간선을 담아준다
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)   # 깊이계산

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))


# def search(x, y):
#     for parentx in parents[x]:
#         for parenty in parents[y]:
#             if parentx == parenty:
#                 return parentx
#
#
# N = int(input())
# parents = [[i] for i in range(N+1)]
#
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     p = min(a, b)
#     c = max(a, b)
#     parents[c] = parents[c] + parents[p]
#
# M = int(input())
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     print(search(a, b))
