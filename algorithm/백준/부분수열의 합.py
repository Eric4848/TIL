from itertools import combinations
N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(1, N + 1):   # 길이가 양수이므로 1개부터 N개까지의 부분집합을 계산
    for comb in combinations([j for j in range(N)], i):
        temp = 0
        for num in comb:
            temp += nums[num]
        if temp == S:
            answer += 1
print(answer)
