import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    is_done = False   # 올바른 달력인지 확인
    # <M-1:N-1> 부터 시작하는 경우에 K = M * a + x = N * b + y를 만족하는 K가 있다고 가정한다
    K = x   # (K-x) % M = 0 , (K-y) % N = 0인 경우를 계산하기 위해 K = x로 초기화한다

    while K <= M * N:   # K의 값은 M * N을 넘을수 없기 때문에
        if (K - x) % M == 0 and (K - y) % N == 0:   # K의 조건을 만족하면
            is_done = True   # 올바름 처리를 하고
            break   # 멈춘다
        K += M   # K를 M으로 나눈 나머지이므로 K에 M을 더해나간다

    if is_done:
        print(K)
    else:
        print(-1)


# 시간초과
# import sys
# import math
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     # M * a + x == N * b + y 가 있는지
#     cnt = 0
#     while cnt < M * N + 1:
#         if x == M and y == N:
#             print(int(M * N / math.gcd(M, N) - cnt))
#             break
#         cnt += 1
#         if x == M:
#             x = 1
#         else:
#             x += 1
#         if y == N:
#             y = 1
#         else:
#             y += 1
#     if cnt == M * N + 1:
#         print(-1)