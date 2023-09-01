# dp로 구현시 메모리 초과
import sys

input = sys.stdin.readline
N = int(input())
matrix = list(map(int, input().split()))
maximum = matrix   # 최댓값을 맨 처음 숫자들로 초기화
minimum = matrix   # 최솟값을 맨 처음 숫자들로 초기화

for _ in range(N-1):   # N-1번
    matrix = list(map(int, input().split()))   # 다음 줄을 입력받아
    maximum = ([matrix[0] + max(maximum[0], maximum[1]), matrix[1] + max(maximum), matrix[2] + max(maximum[1], maximum[2])])   # 각 위치별 기존 최댓값이 올 수 있는 범위만큼 최댓값을 더해준다
    minimum = ([matrix[0] + min(minimum[0], minimum[1]), matrix[1] + min(minimum), matrix[2] + min(minimum[1], minimum[2])])   # 각 위치별 기존 최솟값이 올 수 있는 범위만큼 최솟값을 더해준다
print(max(maximum), min(minimum))
