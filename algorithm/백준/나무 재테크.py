# Pypy3
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
grounds = [[5] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]   # 나무들의 상태를 저장할 리스트 초기화
dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# 초기 나무들 입력
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

# 계산
for _ in range(K):
    # 봄, 여름
    for r in range(N):
        for c in range(N):
            for i in range(len(trees[r][c])-1, -1, -1):   # 나무들의 역순으로(새로운 나무를 뒤에 추가하기 때문)
                if trees[r][c][i] <= grounds[r][c]:   # 영양분이 충분하다면
                    grounds[r][c] -= trees[r][c][i]   # 영양분을 흡수하고
                    trees[r][c][i] += 1   # 나무의 나이를 1살 늘려준다
                else:   # 영양분이 부족하다면
                    for j in range(i, -1, -1):   # 부족한 시점부터 가장 나이 많은 나무까지
                        grounds[r][c] += trees[r][c][j] // 2   # 해당 위치에 영양분으로 바꿔준다
                    trees[r][c] = trees[r][c][i+1:]   # 죽은 나무를 제외한 나무들만 리스트에 담는다
                    break   # 종료(이미 죽은나무 처리했기 때문)

    # 가을
    for r in range(N):
        for c in range(N):
            for age in trees[r][c]:
                if age % 5 == 0:   # 나무들 중 나이가 5의 배수인 나무의 경우
                    for i in range(8):   # 인접한 위치별로
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N:   # 소유한 땅이라면
                            trees[nr][nc].append(1)   # 1살의 나무를 추가한다

    # 겨울
    for r in range(N):
        for c in range(N):
            grounds[r][c] += A[r][c]   # 영양분 공급

answer = 0   # 정답을 초기화
for r in trees:
    for c in r:
        answer += len(c)   # 나무들의 갯수를 정답에 추가

print(answer)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# grounds = [[5] * N for _ in range(N)]
# A = [list(map(int, input().split())) for _ in range(N)]
# trees = deque([])
# dr = [1, 1, 1, 0, 0, -1, -1, -1]
# dc = [-1, 0, 1, -1, 1, -1, 0, 1]
#
# for _ in range(M):
#     r, c, age = map(int, input().split())
#     trees.append([r-1, c-1, age])
#
# for _ in range(K):
#     tmp = deque([])
#     deads = []
#     chks = []
#
#     for r, c, age in trees:
#         if age <= grounds[r][c]:
#             grounds[r][c] -= age
#             age += 1
#             tmp.append([r, c, age])
#             if age % 5 == 0:
#                 chks.append([r, c])
#         else:
#             deads.append([r, c, age // 2])
#
#     for r, c, age in deads:
#         grounds[r][c] += age
#
#     for r, c in chks:
#         for i in range(8):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < N:
#                 tmp.appendleft([nr, nc, 1])
#
#     for r in range(N):
#         for c in range(N):
#             grounds[r][c] += A[r][c]
#
#     trees = tmp
#
# print(len(trees))
