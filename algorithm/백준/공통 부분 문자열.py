# 시간 초과
A = input()
B = input()
L1 = len(A)
L2 = len(B)
dp = [[0 for _ in range(L2)] for _ in range(L1)]
answers = []

for f in range(L1):
    for s in range(L2):
        if A[f] == B[s]:
            dp[f][s] = 1
            i = 1
            while 1:
                if f+i == L1 or s+i == L2:
                    break

                if A[f+i] != B[s+i]:
                    break

                dp[f][s+i] = dp[f][s+i-1] + 1
                i += 1

    answers.append(max(dp[f]))

print(max(answers))
