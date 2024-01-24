import sys

input = sys.stdin.readline
M, N = map(int, input().split())
desks = []   # 각 창구별 걸리는 시간을 담을 리스트
for _ in range(M):
    desks.append(int(input()))

min_time = 1   # 최소 인원 1, 최소 시간 1일 때
max_time = max(desks) * N   # 전체 인원, 최대 시간일 때
# 이분 탐색
while min_time <= max_time:
    checked = 0   # 통과한 사람 수
    mid = (min_time + max_time) // 2   # 중간값 계산

    for desk in desks:   # 각 창구별로
        checked += mid // desk   # 중간값의 시간동안 검사 완료한 수
        if N <= checked:   # 통과한 사람 수가 목표보다 크면
            break   # 종료(이미 다 했으니 계산하지 않아도 된다)

    if N <= checked:   # 총원보다 같거나 많이 검사했으면
        answer = mid   # 정답을 저장해 주고
        max_time = mid-1   # 최대값을 재설정한다
    else:   # 반대의 경우
        min_time = mid + 1   # 최소값을 재설정한다

print(answer)


# 시간 초과
# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
# M, N = map(int, input().split())
# desks = []
# answer = float('inf')
#
# for _ in range(M):
#     desks.append(int(input()))
#
# for perm in permutations(range(N+1), M):
#     if sum(perm) == N:
#         temp = []
#         for i in range(M):
#             temp.append(desks[i] * perm[i])
#         answer = min(answer, max(temp))
#
# print(answer)
