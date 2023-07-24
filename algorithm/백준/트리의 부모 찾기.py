# 시간 초과
import sys
input = sys.stdin.readline
N = int(input())
matrix = []
for _ in range(N-1):
    matrix.append(list(map(int, input().split())))
answer = {}
to_visit = [1]
is_visit = [False] * N
while to_visit:
    for _ in range(len(to_visit)):
        visit = to_visit.pop()
        for i in range(len(matrix)):
            if not is_visit[i]:
                if visit in matrix[i]:
                    for num in matrix[i]:
                        if num != visit:
                            answer[num] = visit
                            to_visit.append(num)
                            is_visit[i] = True
                            break

for i in range(2, N + 1):
    print(answer[i])
