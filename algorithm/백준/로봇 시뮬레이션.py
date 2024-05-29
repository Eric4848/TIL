A, B = map(int, input().split())
N, M = map(int, input().split())
# N, E, S, W (상하반전)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
robots = [[]]   # 로봇 위치를 저장할 리스트
# 로봇 위치 저장
for _ in range(N):
    c, r, d = input().split()
    # 방향 확인
    if d == 'N':
        d = 0
    elif d == 'E':
        d = 1
    elif d == 'S':
        d = 2
    else:
        d = 3
    robots.append([int(r)-1, int(c)-1, d])   # 로봇의 위치와 방향 저장


# 시뮬레이션 하는 함수
def simul():
    for _ in range(M):
        num, order, re = input().split()   # 로봇 번호, 명령, 횟수
        num = int(num)   # 번호와
        re = int(re)   # 횟수를 숫자로 변환
        r, c, d = robots[num]   # 명령을 내릴 로봇 정보 가져오기
        # 명령 확인
        if order == 'L':   # 왼쪽으로라면
            t = -1   # -1
        elif order == 'R':   # 오른쪽으로라면
            t = 1   # 1
        else:   # 이동이라면
            t = 0   # 0
        # 명령 실행
        if t:   # 회전이라면
            d = (d + re * t) % 4   # 현재 방향에서 회전 방향만큼 더해서 4로 나눈 몫을
            robots[num][2] = d   # 로봇 방향에 저장
        else:   # 이동이라면
            for i in range(1, re+1):   # 반복 횟수만큼(이동 거리로 곱할 예정이므로 1 ~ re까지
                nr = r + dr[d] * i   # 새로운 위치
                nc = c + dc[d] * i   # 계산
                if 0 <= nr < B and 0 <= nc < A:   # 이동 위치가 범위 내라면
                    for j in range(1, N+1):   # 로봇별로
                        ar, ac, _ = robots[j]   # 위치를 가져와서
                        if nr == ar and nc == ac:   # 이동한 위치와 같다면
                            return 'Robot ' + str(num) + ' crashes into robot ' + str(j)   # 해당 로봇에 충돌
                else:   # 이동 위치가 범위 바깥이라면
                    return 'Robot ' + str(num) + ' crashes into the wall'   # 벽에 충돌
            # 모든 이동이 끝났다면
            robots[num][0] = nr   # 이동한 위치
            robots[num][1] = nc   # 저장

    return 'OK'   # 명령이 모두 수행 가능


print(simul())
