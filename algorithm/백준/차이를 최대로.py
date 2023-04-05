N = int(input())
array = list(map(int, input().split()))

ans = []
maxx = []

is_used = [False for _ in range(N)]


def dfs():
    if len(ans) == N:
        tmp = 0
        for i in range(N - 1):
            tmp += abs(ans[i] - ans[i + 1])
        maxx.append(tmp)
        return

    for i in range(N):
        if is_used[i]:
            continue
        ans.append(array[i])
        is_used[i] = True
        dfs()
        ans.pop()
        is_used[i] = False


dfs()

print(max(maxx))

# n = int(input())
# a = list(map(int, input().split()))
#
# answer = 0
# is_used = [False for _ in a]
#
#
# def find_sum(maxim, now, count):
#     if count == 5:
#         if maxim > answer:
#             answer = maxim
#         return
#     for i in range(n):
#         if not is_used[i]:
#             temp = abs(now - a[i])
#             is_used[i] = True
#             find_sum(maxim + temp, a[i], count + 1)
#             is_used[i] = False
#
#
# for j in range(n):
#     is_used[j] = True
#     find_sum(0, a[j], 0)
#     is_used[j] = False
#
# print(maximum)
