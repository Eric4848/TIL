from collections import deque

matrix = [deque(list(input())) for _ in range(4)]
N = int(input())
answer = 0
for _ in range(N):
    s, r = map(int, input().split())
    s -= 1
    now = []
    for i in range(4):
        now.append([matrix[i][6], matrix[i][2]])

    if s != 0:
        for i in range(s, 0, -1):
            if now[i][0] != now[i-1][1]:
                if (s-(i-1)) % 2 == 0:
                    matrix[i-1].rotate(r)
                else:
                    matrix[i-1].rotate(-r)
            else:
                break

    if s != 3:
        for i in range(s, 3):
            if now[i][1] != now[i+1][0]:
                if (s-(i+1)) % 2 == 0:
                    matrix[i+1].rotate(r)
                else:
                    matrix[i+1].rotate(-r)
            else:
                break

    matrix[s].rotate(r)
if matrix[0][0] == '1':
    answer += 1
if matrix[1][0] == '1':
    answer += 2
if matrix[2][0] == '1':
    answer += 4
if matrix[3][0] == '1':
    answer += 8

print(answer)
