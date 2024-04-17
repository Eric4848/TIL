import sys

input = sys.stdin.readline
N = int(input())
grounds = [[0 for _ in range(101)] for _ in range(101)]   # 0 <= 좌표 <= 100
# 방향에 맞게 dy, dx 설정
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
answer = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    # 0세대 계산
    grounds[y][x] += 1
    y += dy[d]
    x += dx[d]
    grounds[y][x] += 1
    moves = [d]   # 이동 방향 기록
    for _ in range(g):   # 세대별로
        for i in range(len(moves)-1, -1, -1):   # 여태까지 이동의 역순으로
            nxt = (moves[i]+1) % 4   # 시계방향 90도 회전 후 끝에 이어붙임 -> -1 후 -2 or +2 -> -3 or +1
            # 다음 위치로 이동
            y += dy[nxt]
            x += dx[nxt]
            grounds[y][x] += 1
            moves.append(nxt)   # 이동방향 저장

# 정사각형 확인
for y in range(100):
    for x in range(100):
        if grounds[y][x] and grounds[y+1][x] and grounds[y][x+1] and grounds[y+1][x+1]:
            answer += 1

print(answer)
