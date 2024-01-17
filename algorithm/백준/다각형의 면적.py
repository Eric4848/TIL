import sys

input = sys.stdin.readline
N = int(input())
locs = []
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    locs.append((x, y))
# 원점을 기준으로 신발끈 공식을 사용하기 위해 첫번째 점 위치 추가(맨 마지막, 맨 처음 계산)
locs.append(locs[0])
# 신발끈 공식으로 계산
for i in range(N):
    x1, y1 = locs[i]
    x2, y2 = locs[i+1]
    answer += (x1*y2 - x2*y1) / 2   # 정답에 신발끈으로 계산한 값을 더해준다, 절댓값은 마지막에 취한다(오목 들어가 있는 경우를 게산하기 위해 ex) 시그마 모양)

print(round(abs(answer), 1))   # 정답에 절댓값을 취하고 소수 첫째자리까지 출력한다
