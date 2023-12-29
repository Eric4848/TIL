N = int(input())
rels = list(map(int, input().split()))
leaves = [[] for _ in range(N)]   # 달려있는 하위 노드들을 저장할 리스트
remove = [int(input())]   # 제거할 노드를 리스트로 저장(제거하기 위해)

for i in range(N):   # 노드별로
    # 루트노드 찾기
    if rels[i] == -1:
        root = i
    # 제거할 노드면 넘기기
    elif i == remove[0]:
        continue
    # 상위 노드 번호에 해당 하위 노드 저장
    else:
        leaves[rels[i]].append(i)

# root가 제거되었는지 확인하여 제거되었으면 0 출력
if root == remove[0]:
    print(0)

# root노드만 있는 경우
elif not leaves[root]:
    print(1)

# 그 외의 경우
else:
    # 노드 제거
    while remove:
        delete = remove.pop()   # 제거할 노드를 하나 선택(위치 상관 X)
        remove += leaves[delete]   # 해당 노드의 하위노드들을 제거 리스트에 추가
        leaves[delete] = []   # 제거한 노드의 하위노드들 제거

    # 리프노드 계산
    answer = 0   # 정답을 0으로 초기화
    for leaf in leaves:   # 상위노드별로
        for single in leaf:   # 그 노드의 하위노드별로
            if not leaves[single]:   # 제일 마지막 노드면
                answer += 1   # 정답 1 증가
    print(answer)


# 오답
# N = int(input())
# rels = list(map(int, input().split()))
# leaves = [[] for _ in range(N)]
# answer = 0
#
# for i in range(N):
#     if rels[i] == -1:
#         root = i
#     else:
#         leaves[rels[i]].append(i)
#
# remove = [int(input())]
#
# while remove:
#     delete = remove.pop()
#     remove += leaves[delete]
#     leaves[delete] = []
#
# for leaf in leaves:
#     for single in leaf:
#         if not leaves[single]:
#             answer += 1
#
# if answer:
#     print(answer-1)
# else:
#     print(answer)


# N = int(input())
# edges = list(map(int, input().split()))
# childs = [[] for _ in range(N)]
# answer = 0
# M = int(input())
#
# for i in range(N):
#     if edges[i] == -1:
#         childs[i].append(-1)
#
# for i in range(len(edges)):
#     if edges[i] != -1 and edges[i] != M and childs[edges[i]]:
#         childs[edges[i]].append(i)
#
# childs[M] = []
#
# for child in childs:
#     if childs.index(child) == M:
#         continue
#     for kid in child:
#         if not childs[kid]:
#             answer += 1
#
# print(childs)
# print(answer)
