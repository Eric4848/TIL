T = int(input())
dr1 = [1, -1, 0, 0]
dc1 = [0, 0, 1, -1]
dr2 = [1, 1, -1, -1]
dc2 = [1, -1, 1, -1]

for tc in range(T):
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            tmp = flys[r][c]
            for d in range(4):
                for dist in range(1, M):
                    nr = r + dist * dr1[d]
                    nc = c + dist * dc1[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        tmp += flys[nr][nc]
                    else:
                        break
            if answer < tmp:
                answer = tmp

            tmp = flys[r][c]
            for d in range(4):
                for dist in range(1, M):
                    nr = r + dist * dr2[d]
                    nc = c + dist * dc2[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        tmp += flys[nr][nc]
                    else:
                        break
            if answer < tmp:
                answer = tmp
    print(f'#{tc+1} {answer}')
