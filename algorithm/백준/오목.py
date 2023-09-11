matrix = [list(map(int, input().split())) for _ in range(19)]   # 오목판 상황을 입력
answer = 0   # 이긴 돌을 초기화 한다
dr = [1, 0, 1, -1]   # 행의 이동 경우의 수
dc = [0, 1, 1, 1]    # 열의 이동 경우의 수
for r in range(19):
    for c in range(19):
        if matrix[r][c] != 0:   # 바둑판에 돌이 있으면
            for j in range(4):   # 각 이동방향별로
                if answer == 0:   # 이긴 돌이 없다면
                    for i in range(1, 5):   # 1~4까지
                        if 0 <= r + i * dr[j] < 19 and 0 <= c + i * dc[j] < 19:   # 이동할 수 있으면
                            if matrix[r][c] != matrix[r+i*dr[j]][c+i*dc[j]]:   # 시작 위치와 다른 돌이면
                                break   # 멈춘다
                            if i == 4:   # 5번째까지 돌이 같으면
                                answer = matrix[r][c]   # 그 돌을 이긴 돌로 저장한다
                        if answer:   # 이긴 돌이 있다면
                            if 0 <= r - dr[j] < 19 and 0 <= c - dc[j] < 19:   # 하나 이전과
                                if matrix[r][c] == matrix[r-dr[j]][c-dc[j]]:
                                    answer = 0
                            if 0 <= r + 5 * dr[j] < 19 and 0 <= c + 5 * dc[j] < 19:   # 하나 이후에
                                if matrix[r][c] == matrix[r+5*dr[j]][c+5*dc[j]]:   # 같은 돌이라면
                                    answer = 0   # 이긴 돌에서 빼준다
                    if answer:   # 이긴 돌이 있다면
                        print(answer)   # 이긴 돌을 출력하고
                        print(r+1, c+1)   # 시작 위치를 출력한다

if answer == 0:   # 다 확인 했을 때 이긴 돌이 없다면
    print(answer)   # 초기화된 0을 출력한다
