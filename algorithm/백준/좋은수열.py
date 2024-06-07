# 좋은 수열 판별하는 함수
def check(nxt, l):   # 확인할 수열, 수열 길이
    for j in range(1, l // 2 + 1):   # 1 ~ 길이의 반(내림)
        if nxt[-j:] == nxt[-2*j: -j]:   # 뒤에서부터 해당 길이의 두 수열이 같다면
            return False   # 나쁜 수열
    return True   # 나쁜 수열이 아닌 경우 좋은 수열


# dfs
def dfs(now):   # 현재 수열을 입력받음
    l = len(now)
    if l == N:   # 목표 길이까지 생성했다면
        print(now)   # 현재 수열 출력
        exit()   # 종료
    l += 1   # 길이 1 추가(하나 숫자 하나를 더할 것 이므로)
    for i in range(1, 4):   # 1 ~ 3까지(작은 수로 해야하므로)
        nxt = now + str(i)   # 현재 수열에 문자로 추가
        if check(nxt, l):   # 해당 수열이 좋은 수열이면
            dfs(nxt)   # 그 수열로 dfs 진행


N = int(input())
dfs('1')   # dfs에 1을 넣고 실행


# 시간 초과
# from collections import deque
#
#
# def check():
#     for j in range(1, l // 2 + 1):
#         if nxt[-j:] == nxt[-2*j: -j]:
#             return False
#     return True
#
#
# N = int(input())
# q = deque(['1'])
# while q:
#     now = q.popleft()
#     l = len(now)
#     if len(now) == N:
#         print(now)
#         break
#     l += 1
#     for i in range(1, 4):
#         nxt = now + str(i)
#         if check():
#             q.append(nxt)
