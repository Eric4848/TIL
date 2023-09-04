from collections import deque

matrix = [deque(list(input())) for _ in range(4)]
N = int(input())
answer = 0   # 정답을 0으로 초기화
for _ in range(N):
    s, r = map(int, input().split())
    s -= 1   # 인덱스와 맞추기 위해 1을 빼준다
    now = []   # 각 톱니의 현재 9시, 3시 극성을 저장하기 위한 리스트
    for i in range(4):
        now.append([matrix[i][6], matrix[i][2]])

    if s != 0:   # 제일 왼쪽이 아닌경우
        for i in range(s, 0, -1):   # 시작위치부터 두번째 까지 역순으로
            if now[i][0] != now[i-1][1]:   # 극성이 다르다면
                if (s-(i-1)) % 2 == 0:   # 짝수번째면
                    matrix[i-1].rotate(r)   # 돌린방향으로
                else:   # 홀수번째면
                    matrix[i-1].rotate(-r)   # 반대방향으로 돌려준다
            else:   # 극성이 같다면
                break   # 멈춘다

    if s != 3:   # 제일 오른쪽이 아닌경우
        for i in range(s, 3):   # 시작 위치부터 세번째 까지 순서대로
            if now[i][1] != now[i+1][0]:   # 위와 동일
                if (s-(i+1)) % 2 == 0:
                    matrix[i+1].rotate(r)
                else:
                    matrix[i+1].rotate(-r)
            else:
                break

    matrix[s].rotate(r)   # 시작 톱니를 돌려준다
# 각 위치별로 극성을 확인하여 정답에 더해준다
if matrix[0][0] == '1':
    answer += 1
if matrix[1][0] == '1':
    answer += 2
if matrix[2][0] == '1':
    answer += 4
if matrix[3][0] == '1':
    answer += 8

print(answer)
