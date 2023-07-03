N = int(input())


def top(n, a, b, c):   # 출발, 미사용, 도착 장대 번호를 입력받아
    if n == 0:
        return
    else:
        top(n - 1, a, c, b)   # n-1까지의 원판을 미사용 장대로 이동시키고
        print(a, c)   # 출발 장대에서 도착 장대로 이동시키고
        top(n - 1, b, a, c)   # 미사용 장대로 이동시켜뒀던 원판들을 도착장대로 이동시킨다


print(2 ** N - 1)   # 하노이 탑의 이동 횟수는 n^2 - 1회 이다. (an = n*2 + 1)

top(N, 1, 2, 3)   # 총 N개의 원판을 1에서 3으로 이동시킨다


# def hanoi(n, start, end):
#     if n == 0:
#         return
#     hanoi(n - 1, start, 6 - start - end)
#     print(start, end)
#     hanoi(n - 1, 6 - start - end, end)
#
#
# N = int(input())
# print(N**2 - 1)
# hanoi(N, 1, 3)

# 1 3   1
# 1 2 / 1 3 / 2 1   1*2 + 1
# 1 3 / 1 2 / 3 2 / 1 3 / 2 1 / 2 3 / 1 3   3*2 + 1
# 1 2 / 1 3 / 2 3 / 1 2 / 3 1 / 3 2 / 1 2 / 1 3 / 1 3 / 1 2 / 3 2 / 1 3 / 2 1 / 2 3 / 1 3   7*2 + 1
