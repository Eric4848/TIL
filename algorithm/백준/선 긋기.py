import sys

input = sys.stdin.readline
N = int(input())
spots = [list(map(int, input().split())) for _ in range(N)]
spots.sort()   # 위치를 정렬해준다(시작 위치 기준)
f, l = spots[0]   # 현재 맨앞, 맨뒤를 위치의 첫번째에서 가져온다
total = 0   # 이미 그어진 길이를 0으로 초기화

for i in range(1, N):
    s, e = spots[i]   # 이번 선의 시작, 끝 위치를 가져온다
    if l < s:   # 이전의 끝보다 현재의 시작이 크다면(선이 끊어진다면)
        total += l - f   # 이미 그어진 길이에 현재 맨앞, 맨뒤의 차를 더한다
        f, l = s, e   # 현재 맨앞, 맨뒤를 이번 선의 시작, 끝으로 변경

    else:   # 그렇지 않다면(이어진 선이라면)
        l = max(l, e)   # 맨 뒤를 현재와 가져온 것 중 큰것으로 저장

print(total + l - f)   # 이미 그어진 길이와 현재 맨앞, 맨뒤의 차를 더한다
