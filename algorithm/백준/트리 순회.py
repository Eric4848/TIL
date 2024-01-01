N = int(input())
trees = [[] for _ in range(N)]   # 트리를 저장할 리스트
# 알파벳을 유니코드 변환해 상위 노드에 좌, 우 순서대로 트리에 저장
for _ in range(N):
    M, L, R = map(ord, input().split())
    trees[M-65].append(L-65)
    trees[M-65].append(R-65)
# 전위, 중위, 후위 순으로 순회를 저장할 리스트
fronts = []
middles = []
backs = []


# 전위 순회
def front(n):
    fronts.append(chr(n+65))   # 상위 노드를 전위 리스트에 저장
    for node in trees[n]:   # 좌, 우 하위노드별로
        if 0 <= node:   # '.'이 아니라면
            front(node)   # 해당 노드로 전위 순회


# 중위 순회
def middle(n):
    L = trees[n][0]   # 왼쪽 하위노드
    R = trees[n][1]   # 오른쪽 하위노드
    if 0 <= L:   # 왼쪽 하위노드가 '.'이 아니라면
        middle(L)   # 해당 노드로 중위 순회

    middles.append(chr(n+65))   # 상위 노드를 중위 리스트에 저장

    if 0 <= R:   # 오른쪽 하위노드가 '.'이 아니라면
        middle(R)   # 해당 노드로 중위 순회


# 후위 순회
def back(n):
    for node in trees[n]:   # 하위 노드별로
        if 0 <= node:   # '.'이 아니라면
            back(node)   # 후위 순회
    backs.append(chr(n+65))   # 상위 노드를 후위 리스트에 저장


# 3가지 순회 실행
front(0)
middle(0)
back(0)

# 3가지 순회 출력
print("".join(fronts))
print("".join(middles))
print("".join(backs))
