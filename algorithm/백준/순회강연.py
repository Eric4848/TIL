import sys
import heapq

input = sys.stdin.readline
n = int(input())
answer = 0   # 정답 초기화
q = []   # 힙을 담을 리스트
days = [False] * 10001   # 강의 하는 날 초기화
# 정보 입력
for _ in range(n):
    p, d = map(int, input().split())
    heapq.heappush(q, (-p, d))   # 급여가 큰 순으로 저장하기 위해 힙에 -로 저장
# 강의 계획
while q:
    p, d = heapq.heappop(q)   # 급여기 큰 순서대로 뽑아온다
    for i in range(d, 0, -1):   # 제한 기간 내에(역순으로)
        if not days[i]:   # 강의가 없는 날이 있으면
            answer -= p   # 급여 추가
            days[i] = True   # 해당 날짜 강의함 표시
            break   # 종료

print(answer)


# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
# n = int(input())
# pays = defaultdict(int)
# answer = 0
# for _ in range(n):
#     p, d = map(int, input().split())
#     pays[d] = max(pays[d], p)
# for pay in pays:
#     answer += pays[pay]
# print(answer)
