# 시간 초과
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    answer = 0
    students = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if students[i]:
            tmp = [i, students[i]]
            while True:
                now = tmp.pop()
                nxt = students[now]

                if tmp[0] == now:
                    now = tmp.pop()
                    while True:
                        if students[now] == 0:
                            break
                        students[now] != 0
                        nxt = students[now]
                        students[now] = 0
                        now = nxt

                    break

                if now == nxt:
                    break

                tmp.append(nxt)

    for s in students:
        if s:
            answer += 1

    print(answer)


# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 9)
# T = int(input())
#
#
# def search(num):
#     nxt = students[num]
#
#     if tmp[0] == nxt:
#         for s in tmp:
#             students[s] = 0
#         return
#
#     if tmp[-1] == nxt:
#         return
#
#     tmp.append(nxt)
#     search(nxt)
#
#
# for _ in range(T):
#     n = int(input())
#     answer = 0
#     students = [0] + list(map(int, input().split()))
#     for i in range(1, n+1):
#         if students[i]:
#             tmp = [i]
#             search(i)
#
#     for s in students:
#         if s:
#             answer += 1
#
#     print(answer)
