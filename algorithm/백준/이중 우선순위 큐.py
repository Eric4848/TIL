# 시간 초과
import heapq


def rev(Q):
    temp = []
    for _ in range(len(Q)):
        heapq.heappush(temp, -heapq.heappop(Q))
    return temp


T = int(input())
for _ in range(T):
    flag = 0
    k = int(input())
    q = []
    for _ in range(k):
        order, num = input().split()
        if order == 'I':
            heapq.heappush(q, int(num))

        else:
            if q:
                if int(num) == -1:
                    if flag:
                        q = rev(q)
                        heapq.heappop(q)
                        flag = 0
                    else:
                        heapq.heappop(q)
                else:
                    if flag:
                        heapq.heappop(q)
                    else:
                        q = rev(q)
                        heapq.heappop(q)
                        flag = 1
    if not q:
        print('EMPTY')
    else:
        if flag:
            q = rev(q)
        print(q[0], q[-1])
