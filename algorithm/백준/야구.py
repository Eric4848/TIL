import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
answer = 0   # 정답 초기화
preds = [list(map(int, input().split())) for _ in range(N)]   # 이닝별 결과 저장
# 출전 리스트 구성
for order in permutations(range(1, 9)):   # 첫번쨰 선수를 제외한 8명의 선수 순서 정하기
    orders = list(order) + [0]   # 첫번째 선수 추가
    score = 0   # 현재 순서의 점수 초기화
    number = 5   # 첫번째 선수가 4번타자가 될 수 있게 5번 인덱스로 시작
    for i in range(N):   # 이닝별로
        b1 = 0   # 1루
        b2 = 0   # 2루
        b3 = 0   # 3루
        out = 0   # 아웃 캉누트
        while out < 3:   # 3아웃이 될때까지
            player = orders[number]   # 출전 선수는 리스트의 인덱스 번호
            hit = preds[i][player]   # 해당 선수의 결과
            # 아웃인 경우
            if hit == 0:
                out += 1   # 아웃 + 1
            # 안타인 경우
            elif hit == 1:
                score += b3   # 3루에 값 점수에 추가
                b3 = b2   # 2루가 3루로
                b2 = b1   # 1루가 2루로
                b1 = 1   # 친 선수가 1루로
            # 2루타인 경우
            elif hit == 2:
                score += b3 + b2   # 3루, 2루 값 점수에 추가
                b3 = b1   # 1루가 3루로
                b2 = 1   # 친 선수가 2루로
                b1 = 0   # 1루는 비어있다
            # 3루타인 경우
            elif hit == 3:
                score += b3 + b2 + b1   # 3루, 2루, 1루 값 점수에 추가
                b3 = 1   # 친 선수가 3루로
                b2 = 0   # 2루와
                b1 = 0   # 1루는 비어있다
            # 홈런인 경우
            else:
                score += b3 + b2 + b1 + 1   # 3루, 2루, 1루값 + 타자 1점 점수에 추가
                b3 = 0   # 모든
                b2 = 0   # 베이스는
                b1 = 0   # 비어있다

            number += 1   # 다음 선수로
            number %= 9   # 9의 나머지(9 -> 1 순환)

    answer = max(answer, score)   # 정답과 현 리스트 결과 중 큰 값 저장

print(answer)


# 시간 초과
# import sys
# from itertools import permutations
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# hits = [[] for _ in range(9)]
# answer = 0
# for _ in range(N):
#     preds = list(map(int, input().split()))
#     for i in range(9):
#         hits[i].append(preds[i])
#
# for order in permutations(range(1, 9)):
#     orders = list(order) + [0]
#     score = 0
#     player = 5
#     for i in range(N):
#         bases = deque([0, 0, 0])
#         out = 0
#         while out < 3:
#             tmp = 0
#             now = orders[player]
#             hit = hits[now][i]
#             if not hit:
#                 out += 1
#             else:
#                 bases.appendleft(1)
#                 for _ in range(hit):
#                     tmp += bases.pop()
#                     bases.appendleft(0)
#                 score += tmp
#                 bases.popleft()
#             player += 1
#             player %= 9
#
#     answer = max(answer, score)
#
# print(answer)
