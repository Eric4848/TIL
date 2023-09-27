# 시간 초과
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())


def D(N):
    tmp = int(N)
    tmp = (tmp * 2) % 10000
    return str(tmp)


def S(N):
    tmp = int(N)
    return '9999' if tmp == 0 else str(tmp - 1)


def L(N):
    f = N[0:1]
    return N[1:] + f


def R(N):
    f = N[0:3]
    return N[3:] + f


for _ in range(T):
    A, B = map(int, input().split())
    A = ('0000' + str(A))[-4:]
    q = deque()
    q.append([A, ''])
    tmp = A[0:1]
    A = A[1:]
    while q:
        now, state = q.popleft()
        if int(now) == B:
            print(state)
            break

        q.append([D(now), state + 'D'])
        q.append([S(now), state + 'S'])
        q.append([L(now), state + 'L'])
        q.append([R(now), state + 'R'])


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# T = int(input())
#
#
# def D(N):
#     return (N*2) % 10000
#
#
# def S(N):
#     return 9999 if N == 0 else N-1
#
#
# def L(N):
#     f = N // 1000
#     return (N * 10) % 10000 + f
#
#
# def R(N):
#     e = N % 10
#     return N // 10 + 1000 * e
#
#
# for _ in range(T):
#     A, B = map(int, input().split())
#     q = deque()
#     q.append([A, ''])
#     while q:
#         now, state = q.popleft()
#         if now == B:
#             print(state)
#             break
#
#         q.append([D(now), state + 'D'])
#         q.append([S(now), state + 'S'])
#         q.append([L(now), state + 'L'])
#         q.append([R(now), state + 'R'])
