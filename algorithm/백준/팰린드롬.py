# 시간 초과
import sys

input = sys.stdin.readline
N = int(input())
nums = [0] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    M = E-S
    if M == 0:
        print(1)

    elif M % 2 != 0:
        print(0)

    else:
        for i in range(M//2):
            if nums[S+i] != nums[E-i]:
                print(0)
                break
            if i == M/2 - 1:
                print(1)
