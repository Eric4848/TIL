r1, c1, r2, c2 = map(int, input().split())
answers = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]   # 정답의 크기만큼 리스트 생성
maxnum = 0   # 최대 숫자를 초기화


# 해당 칸의 숫자를 계산하는 함수
def calc(r, c):   # r, c 위치를 입력받음
    l = max(abs(r), abs(c))   # 원점부터 떨어진 거리 l을 계산(r, c중 더 먼 것)
    sq = (l * 2 - 1) ** 2   # l보다 하나 작은 거리의 정사각형
    # 아랫쪽줄인 경우
    if r == l:
        return sq + l * 7 + c   # 내부 사각형 + 아래쪽 중앙까지 길이 + 7 * l + c(정방향)
    # 왼쪽줄인 경우
    elif c == -l:
        return sq + l * 5 + r   # 내부 사각형 + 왼쪽 중앙까지 길이 + 5 * l + r(정방향)
    # 윗쪽줄인 경우
    elif r == -l:
        return sq + l * 3 - c   # 내부 사각형 + 위쪽 중앙까지 길이 + 3 * l - c(역방향)
    # 오른쪽줄인 경우
    else:
        return sq + l - r   # 내부 사각형 + 오른쪽 중앙까지 길이 + l - r(역방향)


for r in range(r1, r2 + 1):   # 조건의 행
    for c in range(c1, c2 + 1):    # 조건의 열
        answers[r - r1][c - c1] = calc(r, c)   # 위치에 맞게 해당 크기 계산하여 저장
        maxnum = max(maxnum, answers[r - r1][c - c1])   # 최대 숫자 비교

maxlen = len(str(maxnum))   # 최대 숫자의 길이
for r in range(r2 - r1 + 1):
    for c in range(c2 - c1 + 1):
        print(str(answers[r][c]).rjust(maxlen), end=' ')   # 가장 긴 길이에 맞춰 우측 정렬하여 출력
    print()   # 줄바꿈


# 시간 초과
# r1, c1, r2, c2 = map(int, input().split())
# answers = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
# total = (c2 - c1 + 1) * (r2 - r1 + 1)
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# d = 1
# r = 0
# c = 0
# cnt = 1
# l = 1
# while total:
#     for _ in range(2):
#         for _ in range(l):
#             if r1 <= r <= r2 and c1 <= c <= c2:
#                 answers[r-r1][c-c1] = cnt
#                 total -= 1
#                 m = cnt
#             r += dr[d]
#             c += dc[d]
#             cnt += 1
#         d = (d-1) % 4
#     l += 1
#
#
# for answer in answers:
#     print(*answer)
