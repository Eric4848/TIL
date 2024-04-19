N, M, K = map(int, input().split())
# 이동방향별 설정
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
grounds = [[[] for _ in range(N)] for _ in range(N)]   # 명령 후 위치를 담을 리스트
fireballs = []   # 파이어볼들을 담을 리스트

# 처음 파이어볼 정보 저장
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(K):   # 명령 횟수만큼
    while fireballs:   # 각 파이어볼마다
        r, c, m, s, d = fireballs.pop()
        # 이동시킨다 / 뒤로 연결되어있으므로 N으로 나눈 나머지
        nr = (r + s * dr[d]) % N
        nc = (c + s * dc[d]) % N
        grounds[nr][nc].append([m, s, d])   # 해당 위치에 질량, 속도, 방향 저장

    for r in range(N):
        for c in range(N):
            # 두 개 이상의 파이어볼이 있는 경우
            if 1 < len(grounds[r][c]):
                mass = 0   # 총 질량
                speed = 0   # 총 속도
                odd = 0   # 총 홀수 방향 갯수
                even = 0   # 총 짝수 방향 갯수
                cnt = len(grounds[r][c])   # 총 파이어볼 갯수
                while grounds[r][c]:   # 해당 칸의 파이어볼이 있다면
                    m, s, d = grounds[r][c].pop()   # 질량, 속도, 방향을 pop한다
                    mass += m   # 질량을 총 질량에 더해준다
                    speed += s   # 속도를 총 속도에 더해준다.
                    # 방향을 저장한다
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                mass = mass // 5   # 질량을 5로 나눈 몫 저장
                speed = speed // cnt   # 속도를 파이어볼 수로 나눈 몫 저장
                # 방향 설정
                if odd == cnt or even == cnt:   # 모두 같다면
                    ds = [0, 2, 4, 6]
                else:   # 다른 것이 있다면
                    ds = [1, 3, 5, 7]
                # 다음 위치로 이동
                if mass:
                    for d in ds:
                        fireballs.append([r, c, mass, speed, d])   # 파이어볼에 저장

            # 파이어볼이 1개라면
            if len(grounds[r][c]) == 1:
                fireballs.append([r, c] + grounds[r][c].pop())   # 파이어볼에 저장

answer = 0
# 정답에 현재 파이어볼의 질량들을 더해준다
for fireball in fireballs:
    answer += fireball[2]

print(answer)
