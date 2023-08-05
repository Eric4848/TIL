N = int(input())
answers = [float('inf') for _ in range(N + 1)]   # 0 ~ N까지 무한으로 초기화한 정답 리스트를 만든다
for i in range(int(N ** 0.5), 0, -1):   # N의 제곱근부터 1까지 하나씩 줄여가며
    answers[i ** 2] = 1   # 그 숫자의 제곱수 갯수를 1로 바꾼다
    for j in range((i ** 2) + 1, N + 1):   # 그 제곱수 다음부터 N까지
        if answers[j - (i ** 2)] + 1 < answers[j]:   # 현 위치의 갯수 합이 계산중인 제곱수 전의 갯수 + 1보다 크다면
            answers[j] = answers[j - (i ** 2)] + 1   # 현 위치의 갯수 합을 바꾼다
print(answers[N])


# 18의 경우 16 + 1 + 1 보다 9 + 9가 더 작다
# N = int(input())
# squares = []
# for i in range(1, int(N ** 0.5) + 1):
#     squares.append(i ** 2)
# answer = 0
# L = len(squares)
# while N:
#     for i in range(L-1, -1, -1):
#         if squares[i] <= N:
#             N -= squares[i]
#             answer += 1
#             break
#         else:
#             squares.pop()
#             L -= 1
# print(answer)
