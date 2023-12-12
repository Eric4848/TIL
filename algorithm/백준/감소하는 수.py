from itertools import combinations

N = int(input())

result = []   # 감소하는 수들을 담을 리스트
for i in range(1, 11):   # 1 ~ 10자리까지
    for j in combinations(range(10), i):   # 0 ~ 9의 숫자를 자릿수별로 조합하여
        num = ''.join(list(map(str, reversed(list(j)))))   # 내림차순으로 정렬하여 합친 후
        result.append(int(num))   # 리스트에 담아준다

result.sort()   # 리스트를 정렬한다
if N >= len(result):
    print(-1)
else:
    print(result[N])

# 시간 초과
# N = int(input())
# if N <= 10:
#     print(N)
# else:
#     cnt = 10
#     i = 11
#     done = 0
#     while i <= 9876543210:
#         nums = str(i)
#         chk = 1
#         for j in range(len(nums)-1):
#             if nums[j] <= nums[j+1]:
#                 chk = 0
#                 break
#         if chk:
#             cnt += 1
#
#         if cnt == N:
#             done = 1
#             print(i)
#             break
#
#         i += 1
#     if not done:
#         print(-1)
# 0 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 40 41 42
