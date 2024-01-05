import sys
import heapq   # 오름차순 정렬을 위해 heapq 사용(문자열의 경우 오름차순 정렬 시 연관 되어있는 숫자와 붙어있게 된다)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    answer = True   # 정답을 일관성이 있다고 초기화 한다
    nums = []   # 번호들을 담을 리스트
    for _ in range(n):
        heapq.heappush(nums, input())   # 번호들을 heap에 넣어준다

    for _ in range(len(nums)-1):   # 번호들 갯수 -1회 만큼
        now = heapq.heappop(nums)   # 현재 번호를 가장 작은 숫자로 pop한다
        if nums[0][:len(now)-1] == now[:-1]:   # 그 다음 작은 숫자와 현재 숫자 길이만큼 비교하여 같다면
            answer = False   # 일관성이 없다고 변경하고
            break   # 확인을 중단한다

    if answer:
        print('YES')
    else:
        print('NO')


# 시간 초과
# import sys
# import heapq
#
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     answer = True
#     nums = [[] for _ in range(10)]
#     for _ in range(n):
#         num = str(input())
#         heapq.heappush(nums[int(num[0])], num)
#
#     for i in range(10):
#         if 1 < len(nums[i]):
#             while nums[i]:
#                 if not answer:
#                     break
#                 now = heapq.heappop(nums[i])
#                 for num in nums[i]:
#                     if num[:len(now)-1] == now[:-1]:
#                         answer = False
#                         break
#
#     if answer:
#         print('YES')
#     else:
#         print('NO')


# 시간 초과
# import sys
# import heapq
#
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     answer = True
#     nums = []
#     for _ in range(n):
#         heapq.heappush(nums, str(input()))
#     while nums:
#         if not answer:
#             break
#         now = heapq.heappop(nums)
#         for num in nums:
#             if num[:len(now)-1] == now[:-1]:
#                 answer = False
#                 break
#     if answer:
#         print('YES')
#     else:
#         print('NO')
