import sys

input = sys.stdin.readline


# 벨먼-포드 알고리즘 => 연결된 모든 간선을 확인
def belman_ford():
    for i in range(N):   # 이동한 횟수
        for now in range(1, N+1):   # 모든 시작점별로
            for nxt, dist in edges[now]:   # 연결된 길, 웜홀들의 도착지와 시간별로
                if dists[now] + dist < dists[nxt]:   # 이동하는 것이 원래 시간보다 짧다면
                    dists[nxt] = dists[now] + dist   # 시간을 갱신한다
                    if i == N - 1:   # 이동횟수가 모든 간선을 이상이면(줄어드는 순환이 있는경우)
                        return True   # True 반환


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = [[] for _ in range(N+1)]   # 길, 웜홀들을 담을 리스트 초기화
    dists = [10001] * (N+1)   # 거리를 10001로 설정(시간이 10000까지이므로 // 무한으로 초기화 하면 음의 순환 생성 불가))

    # 양방향으로 길 추가
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges[s].append((e, t))
        edges[e].append((s, t))

    # 단방향으로 웜홀 추가
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges[s].append((e, -t))

    if belman_ford():
        print("YES")
    else:
        print("NO")


# 오답
# import sys
#
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     N, M, W = map(int, input().split())
#     edges = []
#     chk = 0
#
#     for _ in range(M):
#         s, e, t = map(int, input().split())
#         edges.append((s, e, t))
#         edges.append((e, s, t))
#
#     for _ in range(W):
#         s, e, t = map(int, input().split())
#         edges.append((s, e, -t))
#
#
#     dists = [float('inf')] * (N+1)
#     dists[s] = 0
#     for i in range(1, N+1):
#         for j in range(M*2+W):
#             now, nxt, dist = edges[j]
#
#             if dists[now] + dist < dists[nxt]:
#                 dists[nxt] = dists[now] + dist
#
#                 if i == N:
#                     chk = 1
#                     break
#
#     if chk:
#         print("YES")
#     else:
#         print("NO")
