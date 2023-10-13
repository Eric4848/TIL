n, k = map(int, input().split())
answers = [0] * (k+1)
answers[0] = 1
for _ in range(n):
    num = int(input())
    for i in range(1, k+1):
        if 0 <= i - num:
            answers[i] += answers[i-num]
print(answers[-1])


# 메모리 초과
# n, k = map(int, input().split())
# answers = [[0] * (k+1) for _ in range(n)]   # n X k로 할 필요가 없다
# for i in range(n):
#     answers[i][0] = 1
#     num = int(input())
#     for j in range(1, k+1):
#         answers[i][j] += answers[i-1][j]   # 어차피 윗줄을 그대로 더해야한다
#         if 0 <= j - num:
#             answers[i][j] += answers[i][j-num]
# print(answers[-1][-1])
