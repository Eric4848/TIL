# 시간 초과
import sys

sys.setrecursionlimit(10 ** 9)
codes = input()
nums = [int(code) for code in codes]
answer = [0]
L = len(nums)


def search(i):
    if i == L:
        answer[0] += 1
        return

    if nums[i] == 0:
        return

    search(i+1)

    if nums[i] == 2:
        if nums[i+1] < 7:
            if i < L-1:
                search(i+2)

    if nums[i] == 1:
        if i < L-1:
            search(i+2)


search(0)
print(answer[0])
