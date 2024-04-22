import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]   # 숫자들을 입력받아
nums.sort()   # 정렬한다

answer = nums[-1] - nums[0]   # 정답을 최대 - 최소로 설정(음수도 있기 때문)
left = 0   # 작은 수 인덱스
right = 1   # 큰 수 인덱스

while left < N-1:   # 작은 수가 가장 큰수가 되기 전까지
    diff = nums[right] - nums[left]   # 두 수의 차
    if M <= diff:   # 두 수의 차가 기준보다 큰 경우
        if diff < answer:   # 현재 정답보다 차가 작다면
            answer = diff   # 정답 갱신
        left += 1   # 좌측 인덱스 1개 늘려줌
    else:   # 기준보다 작은 경우
        if right < N-1:
            right += 1
        else:
            left += 1

print(answer)


# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# nums = []
# for _ in range(N):
#     nums.append(int(input()))
#
# nums.sort()
#
# answer = nums[-1]
# left = 0
#
# while left < N-1:
#     for right in range(left+1, N):
#         if M <= nums[right] - nums[left]:
#             if nums[right] - nums[left] < answer:
#                 answer = nums[right] - nums[left]
#             break
#     left += 1
#
# print(answer)
