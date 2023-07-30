import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = 0
    lcm = math.lcm(M, N)
    is_done = False
    while x < lcm and y < lcm:
        if x == y:
            is_done = True
            break
        if x < y:
            x += M
        else:
            y += N

    if is_done:
        print('done')
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