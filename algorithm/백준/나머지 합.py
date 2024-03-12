import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
lefts = [0] * M   # 나머지의 갯수를 저장할 리스트를 0으로 초기화
lefts[nums[0] % M] += 1   # 첫번째 입력의 나머지를 1개 추가

# 누적합,나머지 계산
for i in range(1, N):   # 두번째부터 끝까지
    nums[i] += nums[i-1]   # 이전 합을 더해주고
    lefts[nums[i] % M] += 1   # 그 값의 나머지를 1개 추가

# 조건 계산 => 나머지가 0인경우 처음부터 해당숫자까지의 합 / 나머지가 같은 두 지점 사이의 합
answer = 0   # 정답 초기화
answer += lefts[0]   # 나머지가 0인 숫자들은 자체로 조건을 만족하므로 정답에 추가

# 나머지 0으로 만들어주기
for i in range(M):   # 나머지마다
    cnt = lefts[i]   # 나머지의 갯수
    answer += (cnt * (cnt-1)) // 2   # 해당하는 나머지 중 2개를 선택

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = 0
# for i in range(N-1):
#     nums[i+1] += nums[i]
#
# for e in range(N):
#     if nums[e] % M == 0:
#         answer += 1
#     for s in range(e):
#         if (nums[e] - nums[s]) % M == 0:
#             answer += 1
#
# print(answer)
