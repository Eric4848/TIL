import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline
N, M, K = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]   # 원본 배열
answer = float('inf')   # 정답을 무한으로 초기화


# 회전시키는 함수
def rot(r, c, s):   # 회전 위치와 반경을 입력받아
    tmp1 = matrix[r-s][c+s]   # 오른쪽 위 모서리를 임시저장
    # 위쪽 줄 한칸씩 오른쪽으로
    for i in range(2*s):
        matrix[r-s][c+s-i] = matrix[r-s][c+s-i-1]
    # 왼쪽 줄 한칸씩 위쪽으로
    for i in range(2*s):
        matrix[r-s+i][c-s] = matrix[r-s+i+1][c-s]
    # 아래쪽 줄 한칸씩 왼쪽으로
    for i in range(2*s):
        matrix[r+s][c-s+i] = matrix[r+s][c-s+i+1]
    # 오른쪽 줄 한칸씩 아래쪽으로
    for i in range(2*s):
        matrix[r+s-i][c+s] = matrix[r+s-i-1][c+s]
    # 오른쪽 위 모서리 한칸 아래에 저장한 값 입력
    matrix[r-s+1][c+s] = tmp1


rotations = [list(map(int, input().split())) for _ in range(K)]
# 순열을 사용해 회전 순서별로 계산
for perm in permutations(range(K), K):   # 각 순열별로
    matrix = deepcopy(origin)   # 원본에서 복사해 온 배열
    for i in perm:   # 순열 번호대로
        r, c, s = rotations[i]   # 회전 조건을 가져와
        for j in range(1, s+1):   # 회전반경별로
            rot(r-1, c-1, j)   # 회전
    sums = [sum(matrix[i]) for i in range(N)]   # 각 행별로 합 계산
    answer = min(answer, min(sums))   # 정답과 행별 합의 최소중 작은 것 저장

print(answer)
