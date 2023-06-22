# 브루트포스 방식 => 전체 확인
import sys

input = sys.stdin.readline
channel = int(input())
n = int(input())
disables = list(map(int, input().split()))

min_count = abs(100 - channel)   # 채널을 +,-로 이동한 최소값

for nums in range(1000001):   # 큰 수에서 내려오는 경우도 계산하기 위해 2배까지 계산
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in disables:   # 사용불가 번호를 쓴 경우
            break   # 다음 숫자로
        elif j == len(nums) - 1:   # 만들었으면
            min_count = min(min_count, abs(int(nums) - channel) + len(nums))   # 최솟값과 비교 후 최솟값 저장

print(min_count)


# import sys
#
# now = 100
# channel = str(sys.stdin.readline())
# answer = 0
# n = int(sys.stdin.readline())
# buttons = [True] * 10
# disables = list(map(int, sys.stdin.readline().split()))
# for disable in disables:
#     buttons[disable] = False
#
# for n in range(len(channel)-1):
#     temp = []
#     chan = int(channel[n])
#     if buttons[chan]:
#         answer += 1
#         continue
#     else:
#         if buttons[chan+1] and chan < 10:
#             temp.append(chan+1)
#         if buttons[chan-1] and 0 < chan:
#             temp.append(chan-1)
