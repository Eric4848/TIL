import sys


# 부모를 찾는 함수
def find(N):
    parent = parents[N]
    if parent != N:
        parent = find(parent)
    return parent


# 부모를 합치는 함수
def union(A, B):
    A = find(A)
    B = find(B)
    # 작은 쪽으로 합친다
    if A < B:
        parents[B] = A
    else:
        parents[A] = B


input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n)]   # 자신으로 부모 초기화
answer = 0   # 정답을 0으로 초기화
# 연결
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):   # 두 입력지점이 이어져 있다면(두 지점이 이어져 있어 이으면 원이 되는 경우)
        answer = i + 1   # 정답 변경
        break   # 중단
    union(a, b)   # 두 지점을 합친다

print(answer)
