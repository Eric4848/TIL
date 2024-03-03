import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


# 순회를 확인하는 함수
def search(N):
    global answer

    is_visits[N] = True   # 입력위치를 방문처리
    cycle.append(N)   # 순회에 추가
    nxt = students[N]   # 다음 숫자

    if is_visits[nxt]:   # 다음 위치가 이미 방문한 곳이면
        if nxt in cycle:   # 그 위치가 순회에 있다면
            answer -= len(cycle[cycle.index(nxt):])   # 정답에서 돌아온 위치부터 끝까지의 갯수만큼 빼준다
        return   # 종료

    else:   # 다음 위치가 방문하지 않은 곳이면
        search(nxt)   # 확인


T = int(input())
for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    is_visits = [False] * (n + 1)   # 방문여부를 초기화
    answer = n

    for i in range(1, n+1):   # 각 학생들마다
        if not is_visits[i]:   # 확인하지 않았다면
            cycle = []   # 순회 리스트를 생성하고
            search(i)   # 확인

    print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# T = int(input())
#
# for _ in range(T):
#     n = int(input())
#     answer = n
#     students = [0] + list(map(int, input().split()))
#     for i in range(1, n + 1):
#         if students[i]:
#             tmp = [i, students[i]]
#             while True:
#                 now = tmp.pop()
#                 nxt = students[now]
#
#                 if tmp[0] == now:
#                     now = tmp.pop()
#                     while True:
#                         if students[now] == 0:
#                             break
#                         nxt = students[now]
#                         students[now] = 0
#                         now = nxt
#                         answer -= 1
#
#                     break
#
#                 if now == nxt:
#                     break
#
#                 tmp.append(nxt)
#
#     print(answer)


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
