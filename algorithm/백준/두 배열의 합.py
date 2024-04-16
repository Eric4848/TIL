# defaultdict(자료형) -> 해당 자료형의 모든 key에 기본값 0 생성/int = 0, str = "", list = []
from collections import defaultdict

T = int(input())
NA = int(input())
A = list(map(int, input().split()))
NB = int(input())
B = list(map(int, input().split()))
answer = 0
nums = defaultdict(int)   # int로 defaultdict를 생성

for i in range(NA):   # A배열 시작위치
    for j in range(i, NA):   # A배열 끝 위치
        nums[sum(A[i:j+1])] += 1   # 시작위치 ~ 끝위치까지의 합 갯수 1 추가

for i in range(NB):   # B배열 시작위치
    for j in range(i, NB):   # B배열 끝 위치
        answer += nums[T - sum(B[i:j+1])]   # 목표 값에서 시작위치 ~ 끝위치까지의 합을 뺸 갯수를 정답에 추가

print(answer)


# Index Error(범위가 음수도 있음)
# T = int(input())
# NA = int(input())
# A = list(map(int, input().split()))
# TA = sum(A)+1
# NB = int(input())
# B = list(map(int, input().split()))
# TB = sum(B)+1
# answer = 0
#
#
# tmpA = [0 for _ in range(max(A)+1)]
# tmpB = [0 for _ in range(max(B)+1)]
#
# for a in A:
#     tmpA[a] += 1
# for b in B:
#     tmpB[b] += 1
#
# dpA = [0 for _ in range(TA)]
# dpB = [0 for _ in range(TB)]
#
# A = set(A)
# B = set(B)
#
# for num in A:
#     for i in range(1, TA - num):
#         if dpA[i]:
#             dpA[i+num] = dpA[i]
#     dpA[num] += tmpA[num]
#
# for num in B:
#     for i in range(1, TB - num):
#         if dpB[i]:
#             dpB[i+num] = dpB[i]
#     dpB[num] += tmpB[num]
#
# for i in range(1, T):
#     if NA < i or NB < T-i:
#         continue
#     answer += dpA[i] * dpB[T-i]
#
# print(answer)


# 메모리 초과
# T = int(input())
# NA = int(input())
# LA = list(map(int, input().split()))
# A = set(LA)
# TA = sum(A)+1
# NB = int(input())
# LB = list(map(int, input().split()))
# B = set(LB)
# TB = sum(B)+1
# answer = 0
#
# dpA = [0 for _ in range(TA)]
# dpB = [0 for _ in range(TB)]
#
# tmpA = [0 for _ in range(max(LA)+1)]
# tmpB = [0 for _ in range(max(LB)+1)]
#
# for a in LA:
#     tmpA[a] += 1
# for b in LB:
#     tmpB[b] += 1
#
#
# for num in A:
#     for i in range(1, TA - num):
#         if dpA[i]:
#             dpA[i+num] = dpA[i]
#     dpA[num] += tmpA[num]
#
# for num in B:
#     for i in range(1, TB - num):
#         if dpB[i]:
#             dpB[i+num] = dpB[i]
#     dpB[num] += tmpB[num]
#
# for i in range(1, T):
#     if NA < i or NB < T-i:
#         continue
#     answer += dpA[i] * dpB[T-i]
#
# print(answer)
