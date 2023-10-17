import sys
import heapq

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    minQ, maxQ = [], []   # 최대, 최소를 저장할 힙
    deleted = [True] * k   # 삭제된 입력들을 확인할 리스트
    for i in range(k):
        com, n = input().split()
        n = int(n)
        if com == 'I':
            heapq.heappush(minQ, (n, i))   # 최소
            heapq.heappush(maxQ, (-n, i))   # 최대 힙에 각각 몇번째로 넣었는지와 함꼐 추가
            deleted[i] = False   # 삭제된 입력 리스트 변경
        else:
            if n == 1:   # 최댓값을 빼는 경우
                while maxQ and deleted[maxQ[0][1]]:   # 최댓값 힙에 숫자별로, 해당 숫자가 삭제된 숫자면
                    heapq.heappop(maxQ)   # 해당 숫자를 pop해준다
                if maxQ:   # 그 후 최댓값 힙이 비지 않았으면
                    deleted[maxQ[0][1]] = True   # 삭제함 처리를 하고
                    heapq.heappop(maxQ)   # 최댓값을 제거한다
            else:   # 최솟값을 빼는 경우
                while minQ and deleted[minQ[0][1]]:   # 최댓값과 동일하다
                    heapq.heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heapq.heappop(minQ)

    # 연산이 끝난 후 삭제된 값들 제거
    while minQ and deleted[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and deleted[maxQ[0][1]]:
        heapq.heappop(maxQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')

# 시간 초과
# import heapq
# import sys
#
# input = sys.stdin.readline
#
#
# def rev(Q):
#     temp = []
#     for _ in range(len(Q)):
#         heapq.heappush(temp, -heapq.heappop(Q))
#     return temp
#
#
# T = int(input())
# for _ in range(T):
#     flag = 0
#     k = int(input())
#     q = []
#     for _ in range(k):
#         order, num = input().split()
#         if order == 'I':
#             if not flag:
#                 heapq.heappush(q, int(num))
#             else:
#                 heapq.heappush(q, -int(num))
#
#         else:
#             if q:
#                 if int(num) == -1:
#                     if flag:
#                         q = rev(q)
#                         heapq.heappop(q)
#                         flag = 0
#                     else:
#                         heapq.heappop(q)
#                 else:
#                     if flag:
#                         heapq.heappop(q)
#                     else:
#                         q = rev(q)
#                         heapq.heappop(q)
#                         flag = 1
#     if not q:
#         print('EMPTY')
#     else:
#         if flag:
#             q = rev(q)
#         print(q[-1], q[0])


# 오답
# import heapq
# import sys
#
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     q = []
#     for _ in range(k):
#         print(q)
#         order, num = input().split()
#         if order == 'I':
#             heapq.heappush(q, int(num))
#
#         else:
#             if q:
#                 if int(num) == -1:
#                     heapq.heappop(q)
#                 else:
#                     q.pop()
#
#     if not q:
#         print('EMPTY')
#     else:
#         print(q[-1], q[0])

