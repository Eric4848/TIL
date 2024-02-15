N = int(input())
a, b, c, d, e, f = map(int, input().split())
nums = sorted([min(a, f), min(b, e), min(c, d)])
answer = 0

answer += (5 * N * N - 8 * N + 4) * nums[0]

answer += (N-1) * 8 * nums[1]

answer += 4 * nums[2]

print(answer)
