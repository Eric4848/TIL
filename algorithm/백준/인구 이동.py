import sys

sys.setrecursionlimit(10 ** 9)
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]   # 4방향
dc = [0, 1, 0, -1]   # 이동을 위해
answer = 0


def move(r, c):   # 이동이 가능한 국가를 더하는 함수
    total.append(A[r][c])   # 이동 가능한 국가들의 총 인원에 현재 국가의 인원을 추가
    chk.append((r, c))   # 분배를 위해 국가의 위치도 저장한다
    is_able[r][c] = False   # 다시 이동을 확인하지 않도록 False로 바꿔준다
    for d in range(4):   # 각 방향별로
        nr = r + dr[d]
        nc = c + dc[d]
        if nr == N or nc == N or nr == -1 or nc == -1:   # 범위를 벗어나면
            continue   # 다음 방향으로 이동
        if is_able[nr][nc]:   # 이동이 가능하고
            if L <= abs(A[r][c] - A[nr][nc]) <= R:   # 인구 이동이 가능한 범위면
                move(nr, nc)   # 해당 위치로 다시 함수 실행


while True:
    flag = 0   # 인구 이동여부를 확인
    is_able = [[True] * N for _ in range(N)]   # 인구이동이 가능한지를 매 반복마다 초기화
    for i in range(N):
        for j in range(N):
            if is_able[i][j]:   # 인구이동이 가능한 국가면
                total = []   # 이동가능 인원의 총합
                chk = []   # 인구이동할 국가들의 위치
                move(i, j)   # 현재 위치를 이동 가능 국가로 더해준다
                if 1 < len(total):   # 이동가능 국가들의 수가 2개 이상이면
                    flag = 1   # 인구이동이 일어난다
                shared = sum(total) // len(total)   # 나누어 갖는 인구수
                for rr, rc in chk:   # 인구이동하는 국가별로
                    A[rr][rc] = shared   # 인구수를 재설정해준다
    if not flag:   # 이동이 없었다면
        print(answer)   # 정답을 출력하고
        break   # 반복문을 종료한다
    else:   # 이동이 있었다면
        answer += 1   # 정답에 1일을 추가한다
