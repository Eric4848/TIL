import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
answers = [[0] * N for _ in range(N)]   # 팰린드롬인지를 저장할 리스트를 0으로 초기화한다
M = int(input())
for d in range(N):   # 시작 지점에서 몇 칸까지 계산할 지의 거리
    for f in range(N):   # 시작지점
        l = f + d   # 끝지점
        if N <= l:   # 끝지점이 숫자들을 넘어가면
            continue   # 넘어간다

        if d == 0:   # 거리가 0 => 숫자 하나인 경우
            answers[f][l] = 1   # 해당지점은 팰린드롬이다

        elif nums[f] == nums[l]:   # 시작지점과 끝지점이 팰린드롬인 경우
            if d == 1:   # 거리가 1(숫자 2개인 경우)
                answers[f][l] = 1   # 팰린드롬이다

            elif answers[f+1][l-1] == 1:   # 그 외의 경우 맨앞의 다음뷰터 맨뒤의 이전이 팰린드롬이면
                answers[f][l] = 1   # 그 숫자들도 팰린드롬이다


for _ in range(M):
    S, E = map(int, input().split())
    print(answers[S-1][E-1])   # 해당 지점이 팰린드롬인지 출력한다

# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# nums = [0] + list(map(int, input().split()))
# M = int(input())
# for _ in range(M):
#     S, E = map(int, input().split())
#     M = E-S
#     if M == 0:
#         print(1)
#
#     elif M % 2 != 0:
#         print(0)
#
#     else:
#         for i in range(M//2):
#             if nums[S+i] != nums[E-i]:
#                 print(0)
#                 break
#             if i == M/2 - 1:
#                 print(1)
