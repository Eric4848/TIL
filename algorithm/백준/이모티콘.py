# 오답
S = int(input())
dp = [i for i in range(S+2)]
dp[1] = 0
for i in range(3, S+2):
    dp[i-1] = min(dp[i-1], dp[i] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 2, dp[i])

    jump = 2
    for j in range(2*i, S+2, i):
        dp[j] = dp[i] + jump
        jump += 1

print(dp[S])

# 메모리 초과
# from collections import deque
#
# S = int(input())
# q = deque([(0, 1, 0)])
# while q:
#     time, smiles, clips = q.popleft()
#     if smiles == S:
#         print(time)
#         break
#
#     q.append((time+1, smiles, smiles))
#
#     q.append((time+1, smiles + clips, clips))
#
#     q.append((time+1, smiles - 1, clips))
#
