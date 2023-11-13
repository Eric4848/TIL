from collections import deque

N = int(input())
M = int(input())
roads = [list(map(int, input().split())) for _ in range(N)]   # 출발지에서 도착할 수 있는 도시가 1인 리스트
plans = list(map(int, input().split()))   # 방문할 도시
answer = 'YES'   # 정답을 가능하다고 설정


for i in range(M - 1):   # 방문 도시개수-1번 만큼
    s = plans[i] - 1   # 출발
    e = plans[i + 1] - 1   # 도착
    chk = 0   # 길이 없다고 초기화
    is_visit = [False] * N   # 방문하지 않았다고 초기화
    is_visit[s] = True   # 출발지를 방문처리
    q = deque([s])   # 출발지를 deque에 추가
    while q:
        now = q.popleft()   # 출발지 리스트에서 하나 leftpop하여
        if now == e:   # 도착지라면
            chk = 1   # 갈 수 있다
            break

        for to in range(N):   # 각 도시별로
            if not is_visit[to] and roads[now][to]:   # 방문하지 않았고 현재 도시에서 그 도시로 갈 수 있다면
                is_visit[to] = True   # 그 도시를 방문처리
                q.append(to)   # 그도시를 출발지에 추가

    if not chk:   # 출발지에서 도착지에 가지 못한다면
        answer = 'NO'   # 정답을 불가능하다고 바꾸고
        break   # 계획별 가능여부 확인 중단

print(answer)
