import sys

input = sys.stdin.readline
N = int(input())
answer = 0   # 만족도 초기화
sits = [[0] * N for _ in range(N)]   # 좌석을 0으로 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
students = [list(map(int, input().split())) for _ in range(N**2)]
locs = []   # 학생 자리의 위치를 저장할 리스트
# 위치 배정
for student in students:
    s = student[0]    # 해당 학생과
    likes = student[1:]   # 학생의 선호학생
    info = [0, 0, -1, 0]   # r, c, 좋아하는 학생 수(좋아하는 학생이 없는 위치도 찾아내기 위해 -1), 주위 빈칸을 초기화
    # 모든 위치를 돌며
    for r in range(N):
        for c in range(N):
            if sits[r][c]:   # 해당 자리에 주인이 있으면
                continue   # 넘어간다

            like = 0   # 해당 위치 주변의 좋아하는 학생 초기화
            empty = 0   # 해당 위치 주변의 빈칸 초기화
            for i in range(4):   # 4방향별로
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:   # 범위 내이며
                    if sits[nr][nc] in likes:   # 좋아하는 학생이 있다면
                        like += 1   # 추가

                    elif not sits[nr][nc]:   # 비어있다면
                        empty += 1   # 추가

            if info[2] < like:   # 좋아하는 학생 수가 저장된 것 보다 크다면
                info = [r, c, like, empty]   # 정보 변경

            elif info[2] == like and info[3] < empty:   # 좋아하는 수가 같고 빈 자리가 더 많다면
                info = [r, c, like, empty]   # 정보 변경

    sits[info[0]][info[1]] = s   # 저장된 위치에 학생 배치
    locs.append((info[0], info[1]))   # 위치정보 저장

# 만족도 계산
for i, loc in enumerate(locs):
    r, c = loc
    like = 0   # 주변에 좋아하는 학생 수 초기화
    likes = students[i][1:]
    for j in range(4):   # 4방향별로
        nr = r + dr[j]
        nc = c + dc[j]
        if 0 <= nr < N and 0 <= nc < N and sits[nr][nc] in likes:   # 좋아하는 사람이면
            like += 1   # 좋아하는 수 + 1

    if like:   # 좋아하는 학생이 있다면
        answer += 10 ** (like-1)   # 만족도를 더해준다

print(answer)
