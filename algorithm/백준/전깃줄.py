N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()   # 전깃줄을 A의 순서대로 정렬한다
# LIS -> 가장 긴 부분이 증가하는 수열
LIS = [1] * N   # LIS를 하기 위해 1로 초기화한다
for i in range(1, N):   # 끝 위치는 길이가 2 이상은 되어야 하므로 1부터 N까지
    for j in range(i):   # 처음부터 끝위치까지
        if lines[j][1] < lines[i][1]:   # 탐색 끝보다 현재 위치가 더 작다면
            LIS[i] = max(LIS[i], LIS[j] + 1)   # 끝위치에 저장되어있던 LTS와 현재 위치의 LTS+1중 큰것을 저장한다

print(N - max(LIS))   # 제거해야할 전선 갯수 = 총 입력갯수 - 증가하는 최장길이
