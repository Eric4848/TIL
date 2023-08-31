# 속도를 위해 값을 미리 저장, 범위가 0~20만 필요함, 3개의 값중 어떤 것이든 0이면 1을 저장
matrix = [[[1 if i == 0 or j == 0 or k == 0 else 0 for i in range(21)] for j in range(21)] for k in range(21)]
for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            # 조건에 맞춰 값을 저장해준다
            if a < b < c:
                matrix[a][b][c] = matrix[a][b][c-1] + matrix[a][b-1][c-1] - matrix[a][b-1][c]
            else:
                matrix[a][b][c] = matrix[a-1][b][c] + matrix[a-1][b-1][c] + matrix[a-1][b][c-1] - matrix[a-1][b-1][c-1]
while 1:
    a, b, c = map(int, input().split())
    x = a
    y = b
    z = c
    if a == b == c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:   # 0이하가 있는 경우 먼저
        a = b = c = 0

    elif 20 < a or 20 < b or 20 < c:   # 20초과가 있는 경우
        a = b = c = 20

    print(f"w({x}, {y}, {z}) = {matrix[a][b][c]}")
