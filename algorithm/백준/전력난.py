import sys
import heapq


# 부모를 찾는 함수
def find(N):
    parent = parents[N]
    if parent != N:
        parent = find(parent)
    return parent


# 두 부모를 합치는 함수
def union(A, B):
    A = find(A)
    B = find(B)
    if A < B:
        parents[B] = A
    else:
        parents[A] = B


input = sys.stdin.readline
while True:
    m, n = map(int, input().split())

    # 종료 조건
    if m == n == 0:
        break

    q = []   # 거리, 비용을 힙으로 저장할 리스트
    total = 0   # 총 비용 초기화
    answer = 0   # 사용할 비용 초기화
    parents = [i for i in range(m)]   # 부모를 자신으로 설정
    cnt = 0   # 계산 횟수 초기화

    # 간선들을 힙으로 저장
    for _ in range(n):
        x, y, z = map(int, input().split())
        heapq.heappush(q, (z, x, y))   # 힙에 비용과 두 지점 순으로 저장
        total += z   # 총 비용에 비용 추가

    # 계산
    while cnt < m - 1:   # m-1번 선택할 동안
        d, a, b = heapq.heappop(q)   # 힙에서 pop한다
        if find(a) != find(b):   # 두 지점이 연결되지 않았다면
            answer += d   # 사용할 비용에 비용 추가
            union(a, b)   # 두 지점 연결
            cnt += 1   # 선택횟수 1증가

    print(total - answer)   # 총량에서 사용량을 빼 출력
