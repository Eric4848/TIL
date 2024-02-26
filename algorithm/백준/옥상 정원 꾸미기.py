import sys

input = sys.stdin.readline
N = int(input())
buildings = [int(input()) for _ in range(N)]
answer = 0
stack = []   # 스택을 초기화

# 자신을 볼 수 있는 이전 건물의 갯수 계산
for building in buildings:   # 건물들 별로
    while stack and stack[-1] <= building:   # 건물이 있고, 현재 건물이 이전 건물보다 크거나 같다면
        stack.pop()   # 제거해 준다
    stack.append(building)   # 현재 건물 추가

    answer += len(stack) - 1   # 정답에 현재 건물을 제외한 이전 건물 수 만큼 더해준다

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# buildings = [int(input()) for _ in range(N)]
# answer = 0
#
# for s in range(N-1):
#     view = buildings[s]
#     for chk in range(s+1, N):
#         if view <= buildings[chk]:
#             break
#
#         if buildings[chk] < view:
#             answer += 1
#
# print(answer)
