import sys
from itertools import combinations


# 현재 그룹이 연결되어있는지 확인하는 함수
def search(groups):
    q = [groups[0]]   # 큐에 입력된 지역 중 첫번째를 넣어준다
    is_visit = [False] * N   # 방문여부를 초기화 한다
    is_visit[groups[0]] = True   # 큐에 있는 지역을 방문처리한다
    while q:
        now = q.pop()   # 연결된 지역 중 하나를 pop한다
        for near in nears[now][1:]:   # 그 지역과 연결된 지역들 중([0]는 갯수이므로 사용하지 않는다)
            if near-1 in groups and not is_visit[near-1]:   # 입력된 지역과 이어져 있고 방문하지 않았다면(index로 계산중이므로-1)
                is_visit[near-1] = True   # 방문처리 후
                q.append(near-1)   # 큐에 넣어준다

    if sum(is_visit) == len(groups):   # 방문 지역수가 입력 지역 수와 같다면
        return True   # True
    else:   # 아니면
        return False   # False


input = sys.stdin.readline
N = int(input())
populations = list(map(int, input().split()))   # 지역 별 인구수
nears = [list(map(int, input().split())) for _ in range(N)]   # 인접한 지역([0]는 사용하지 않음)
answer = float('inf')   # 정답을 무한으로 초기화

for i in range(1, N // 2 + 1):   # 1개부터 전체 지역의 반까지(버림 -> 나머지가 자연스레 반대지역이 되므로)
    combs = combinations(range(N), i)   # 갯수별로 조합하여
    for comb in combs:   # 조합별로
        opos = set([i for i in range(N)]) - set(comb)   # 반대 지역을 set을 활용해 계산한다
        if search(comb) and search(list(opos)):   # 두 그룹의 연결 여부를 각각 확인하여 둘 다 연결되었다면(set으로 입력하면 오류)
            temp = 0   # 임시 합을 0으로 초기화
            for j in range(N):   # 모든 지역별로
                if j in comb:   # 첫번째 지역에 있으면
                    temp += populations[j]   # 더하고
                else:   # 두번째 지역에 있으면
                    temp -= populations[j]   # 뺀다
            answer = min(answer, abs(temp))   # 정답과 임시합의 절댓값 중 작은 것 저장

if answer == float('inf'):
    print(-1)
else:
    print(answer)


# 오답
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
# N = int(input())
# populations = list(map(int, input().split()))
# nears = [list(map(int, input().split())) for _ in range(N)]
# answer = float('inf')
# for i in range(1, N // 2 + 1):
#     combs = combinations(range(N), i)
#     for comb in combs:
#         is_visited = [False] * N
#         opos = []
#         temp = 0
#
#         for area in comb:
#             temp += populations[area]
#             for link in nears[area][1:]:
#                 if link - 1 in comb and not is_visited[area]:
#                     is_visited[area] = True
#
#         if sum(is_visited) != i:
#             continue
#
#         for j in range(N):
#             if not is_visited[j]:
#                 opos.append(j)
#
#         for area in opos:
#             temp -= populations[area]
#             for link in nears[area][1:]:
#                 if link - 1 in opos and not is_visited[area]:
#                     is_visited[area] = True
#
#         if False in is_visited:
#             continue
#
#         answer = min(answer, abs(temp))
#
# if answer == float('inf'):
#     print(-1)
# else:
#     print(answer)
