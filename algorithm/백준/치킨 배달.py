from itertools import combinations
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')   # 최소 거리가 정답이므로 무한으로 초기화
chickens = []   # 치킨집 위치들을 저장할 리스트
distances = []   # 각 집의 거리들을 저장할 리스트

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chickens.append((i, j))   # 치킨집 위치를 찾아서 저장

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            temp = []   # 해당 집의 치킨집 별 거리를 잠시 저장할 리스트
            for k in range(len(chickens)):   # 치킨집 별로
                temp.append(abs(chickens[k][0] - i) + abs(chickens[k][1] - j))   # 거리를 계산해서 리스트에 넣어서
            distances.append(temp)   # 집별 거리 리스트에 저장

for comb in combinations([i for i in range(len(chickens))], M):   # 총 치킨집들 중 M개만을 선택하여 조합별로
    summary = 0   # 조합의 거리합을 0으로 초기화 하고
    for i in range(len(distances)):   # 각 집별로
        temp = []   # 살아남은 치킨집들의 거리를 저장할 리스트
        for j in range(len(chickens)):   # 치킨집들 중
            if j in comb:   # 이번에 살아남은 치킨집이라면
                temp.append(distances[i][j])   # 그 치킨집과의 거리를 저장할 리스트에 추가한다
        summary += min(temp)   # 거리들중 최솟값을 이번 조합의 거리합에 추가한다
    if summary < answer:   # 정답으로 한 것 보다 작다면
        answer = summary   # 정답을 변경해준다

print(answer)
