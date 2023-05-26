N = int(input())

arrays = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arrays[i] > arrays[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# # dfs - 시간초과
# N = int(input())
# arrays = list(map(int, input().split()))
# is_used = [False] * N
#
# maximum = [-float('INF')]
# ans = [0]
#
#
# def dfs(s, cnt):
#     if max(ans) > cnt + N - s:
#         return
#
#     if s == N:
#         ans.append(cnt)
#         return
#
#     for i in range(s, N):
#         if arrays[i] > maximum[-1] and not is_used[i]:
#             is_used[i] = True
#             maximum.append(arrays[i])
#             dfs(i+1, cnt+1)
#             is_used[i] = False
#             maximum.pop()
#
#
# dfs(0, 0)
# print(max(ans))
