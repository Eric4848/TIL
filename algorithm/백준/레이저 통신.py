from collections import deque

W, H = map(int, input().split())
grounds = [list(input().strip()) for _ in range(H)]
targets = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque([])

for r in range(H):
    for c in range(W):
        if grounds[r][c] == 'C':
            targets.append((r, c))
        elif grounds[r][c] == '.':
            grounds[r][c] = float('inf')

grounds[targets[0][0]][targets[0][1]] = -1
grounds[targets[1][0]][targets[1][1]] = float('inf')
q.append([targets[0][0], targets[0][1], 4])

while q:
    r, c, d = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < H and 0 <= nc < W and grounds[nr][nc] != '*':
            cnt = grounds[r][c]
            if i != d and cnt + 1 <= grounds[nr][nc]:
                q.append((nr, nc, i))
                grounds[nr][nc] = cnt + 1
            elif i == d and cnt <= grounds[nr][nc]:
                q.appendleft((nr, nc, i))
                grounds[nr][nc] = cnt

print(grounds[targets[1][0]][targets[1][1]])
for g in grounds:
    print(*g)
