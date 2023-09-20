# Union-Find = 합집합 연산, 찾기 연산
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N, M = map(int, input().split())
parents = [i for i in range(N + 1)]   # 부모 노드를 자신으로 설정


def findParent(x):   # 부모 노드를 찾는 함수
    if parents[x] != x:   # 부모 노드가 자기 자신이 아닌경우
        parents[x] = findParent(parents[x])   # 그 다음 부모 노드를 찾아서 저장한다
    return parents[x]   # 부모노드가 자기 자신인 경우 그 값을 반환한다(재귀 끝)


def unionParent(a, b):   # 부모 노드를 합치는 함수
    a = findParent(a)   # 입력된 두 숫자 각각의
    b = findParent(b)   # 부모 노드를 찾는다
    if a < b:   # 더 작은 숫자를
        parents[b] = a   # 큰 숫자의 부모 노드로 설정한다
    else:
        parents[a] = b


for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:   # 두 수를 합치는 경우
        unionParent(a, b)   # 부모 노드를 연결한다
    else:   # 같은 집합인지 확인하는 경우
        if findParent(a) == findParent(b):   # 두 수의 부모 노드(공유하는 가장 작은 수)가 같은지 확인한다
            print('YES')
        else:
            print('NO')

# 시간 초과(2%)
# import heapq
# import sys
#
# input= sys.stdin.readline
# N, M = map(int, input().split())
# sets = [[i] for i in range(N+1)]
# heapq.heapify(sets)
# for _ in range(M):
#     c, a, b = map(int, input().split())
#     if c == 0:
#         if a != b:
#             chk = 0
#             tmp = []
#             heapq.heapify(tmp)
#             for _ in range(len(sets)):
#                 if a in sets[0] or b in sets[0]:
#                     if chk == 0:
#                         inc = heapq.heappop(sets)
#                         chk = 1
#                     else:
#                         heapq.heappush(tmp, inc + heapq.heappop(sets))
#                 else:
#                     heapq.heappush(tmp, heapq.heappop(sets))
#             sets = tmp
#
#     else:
#         chk = 0
#         for i in range(len(sets)):
#             if a in sets[i]:
#                 if b in sets[i]:
#                     print('YES')
#                     chk = 1
#                     break
#         if not chk:
#             print('NO')


# 시간 초과
# N, M = map(int, input().split())
# sets = [[i] for i in range(N+1)]
# for _ in range(M):
#     c, a, b = map(int, input().split())
#     if c == 0:
#         if a != b:
#             for i in range(len(sets)):
#                 if a in sets[i]:
#                     tmp = sets.pop(i)
#                     for j in range(len(sets)):
#                         if b in sets[j]:
#                             sets[j] += tmp
#                             break
#                     break
#
#     else:
#         chk = 0
#         for i in range(len(sets)):
#             if a in sets[i]:
#                 if b in sets[i]:
#                     print('YES')
#                     chk = 1
#                     break
#         if not chk:
#             print('NO')
