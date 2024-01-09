import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]   # 숫자판을 입력받는다
answers = [[0] * m for _ in range(n)]   # 가장 큰 정사각형의 한 변 길이를 담을 리스트를 초기화
answers[0] = maps[0]   # 첫째줄을 숫자판에서 가져온다
answer = 0

for r in range(1, n):   # 둘째줄부터
    answers[r][0] = maps[r][0]   # 맨 앞 숫자를 숫자판에서 가져온다
    for c in range(1, m):   # 둘째칸부터
        if maps[r][c]:   # 그 칸이 정사각형이 될 수 있다면
            # 왼쪽, 왼쪽 위, 위 방향의 이전 칸이 왼쪽, 왼쪽 위, 오른쪽 방향으로 생성 가능한 정사각형의 최대이므로 그 값들 중 최소 + 1이 현재의 최대가 된다
            answers[r][c] = min(answers[r-1][c], answers[r][c-1], answers[r-1][c-1]) + 1   # 이전칸 중 최솟값 + 1을 저장한다

for i in range(n):   # 줄별로
    answer = max(answer, max(answers[i]))   # 각 줄의 최댓값과 정답 중 큰 값을 정답에 저장

print(answer ** 2)   # 넓이를 출력


# 오답
# n, m = map(int, input().split())
# maps = [list(map(int, input().strip())) for _ in range(n)]
# answer = 0
# for r in range(1, n):
#     for c in range(1, m):
#         if answer <= maps[r][c]:
#             chk = 1
#             for i in range(maps[r-1][c-1]):
#                 if not maps[r-1-i][c] or not maps[r][c-1-i]:
#                     chk = 0
#                     break
#
#             if chk:
#                 maps[r][c] = maps[r-1][c-1] + 1
#                 answer = max(answer, maps[r][c])
# print(answer)


# 시간 초과
# n, m = map(int, input().split())
# maps = [list(map(int, input().strip())) for _ in range(n)]
# answer = 0
# for r in range(1, n):
#     for c in range(1, m):
#         if maps[r][c]:
#             chk = 1
#             for i in range(maps[r-1][c-1]):
#                 if not maps[r-1-i][c] or not maps[r][c-1-i]:
#                     chk = 0
#                     break
#
#             if chk:
#                 maps[r][c] = maps[r-1][c-1] + 1
#                 answer = max(answer, maps[r][c])
# print(answer)
