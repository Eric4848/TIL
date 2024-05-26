N = int(input())
K = int(input())
roads = sorted(map(int, input().split()))   # 거리를 입력받아 순서대로 정렬
# 집중국 갯수와 센서 갯수 비교
if N <= K:   # 집중국이 센서보다 같거나 많다면
    print(0)   # 0 (모든 센서에 집중국 설치)
else:   # 집중국이 더 적다면
    dists = []   # 거리를 저장할 리스트
    for i in range(1, len(roads)):   # 센서간 거리 저장
        dists.append(roads[i] - roads[i-1])
    dists.sort()   # 거리를 정렬
    print(sum(dists[:N-K]))   # 기지국 갯수만큼 먼 것을 빼고 더해준다
