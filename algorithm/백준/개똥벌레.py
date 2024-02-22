import sys

input = sys.stdin.readline
N, H = map(int, input().split())
B = [0] * (H+1)   # 석순 크기별 갯수를 0으로 초기화(0~H)
T = [0] * (H+1)   # 종유석 크기별 갯수를 0으로 초기화(0~H)
minimum = N   # 부숴야하는 최소 갯수를 N개로 초기화
counts = 0   # 이동경로 갯수 0으로 초기화

# 석순, 종유석 순으로 저장
for i in range(N // 2):   # 전체 길이의 반만큼
    B[int(input())] += 1   # 해당 석순 크기 1개 증가
    T[int(input())] += 1   # 해당 종유석 크기 1개 증가

# 막히는 칸 계산
for i in range(H, 1, -1):   # 길이가 H부터 2까지 자신의 갯수 만큼 아래 길이의 갯수에 추가해준다
    B[i-1] += B[i]
    T[i-1] += T[i]

# 부숴야 하는 갯수 계산
for i in range(1, H+1):   # 각 높이별로
    if B[i] + T[H-i+1] < minimum:   # 석순의 해당 높이의 갯수 + 종유석의 천장에서 - 해당 높이의 갯수가 최소치보다 작다면
        minimum = T[i] + B[H-i+1]   # 최소치 변경
        counts = 1   # 갯수를 1개로 변경
    elif B[i] + T[H-i+1] == minimum:   # 석순의 해당 높이의 갯수 + 종유석의 천장에서 - 해당 높이의 갯수가 최소치와 같다면
        counts += 1   # 갯수 1개 추가

print(minimum, counts)


# 시간 초과
# N, H = map(int, input().split())
# answers = [0] * H
#
# for i in range(N):
#     L = int(input())
#     if i % 2 == 0:
#         for j in range(L):
#             answers[j] += 1
#
#     else:
#         for j in range(L):
#             answers[H-1-j] += 1
#
# minimum = min(answers)
# cnt = 0
#
# for answer in answers:
#     if answer == minimum:
#         cnt += 1
#
# print(minimum, cnt)


# 메모리 초과
# N, H = map(int, input().split())
# caves = [[False] * N for _ in range(H)]
# maxlen = N
# answer = 0
#
# for i in range(N):
#     L = int(input())
#     if i % 2 == 0:
#         for j in range(L):
#             caves[H-1-j][i] = True
#
#     else:
#         for j in range(L):
#             caves[j][i] = True
#
# for cave in caves:
#     total = sum(cave)
#     if total == maxlen:
#         answer += 1
#
#     elif total < maxlen:
#         maxlen = total
#         answer = 1
#
# print(maxlen, answer)
