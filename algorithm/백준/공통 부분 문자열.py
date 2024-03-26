# Pypy
import sys

input = sys.stdin.readline
A = input().rstrip()
B = input().rstrip()
L1 = len(A)
L2 = len(B)
dp = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)]   # L1+1 X L2+1 크기의 dp를 0으로 초기화
answer = 0

for i in range(1, L1+1):
    for j in range(1, L2+1):
        if A[i-1] == B[j-1]:   # 각 위치의 문자열이 같다면
            dp[i][j] = dp[i-1][j-1] + 1   # 각위치 이전칸의 공통 문자열의 갯수 + 1로 저장
            answer = max(answer, dp[i][j])   # 정답과 비교하여 큰 것 저장

print(answer)


# 오답
# A = input()
# B = input()
# L1 = len(A)
# L2 = len(B)
# dp = [[0 for _ in range(L2)] for _ in range(L1)]
# answers = []
#
# for f in range(L1):
#     s = 0
#     while s < L2:
#         if A[f] == B[s]:
#             dp[f][s] = 1
#             i = 1
#             while 1:
#                 if f+i == L1 or s+i == L2:
#                     break
#
#                 if A[f+i] != B[s+i]:
#                     break
#
#                 dp[f][s+i] = dp[f][s+i-1] + 1
#                 i += 1
#             s += i
#         else:
#             s += 1
#
#     answers.append(max(dp[f]))
#
# print(max(answers))


# 시간 초과
# A = input()
# B = input()
# L1 = len(A)
# L2 = len(B)
# dp = [[0 for _ in range(L2)] for _ in range(L1)]
# answers = []
#
# for f in range(L1):
#     for s in range(L2):
#         if A[f] == B[s]:
#             dp[f][s] = 1
#             i = 1
#             while 1:
#                 if f+i == L1 or s+i == L2:
#                     break
#
#                 if A[f+i] != B[s+i]:
#                     break
#
#                 dp[f][s+i] = dp[f][s+i-1] + 1
#                 i += 1
#
#     answers.append(max(dp[f]))
#
# print(max(answers))
