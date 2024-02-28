# 위상정렬
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    reqs = [0] * (N+1)   # 건설에 필요한 이전 건물 갯수를 0으로 초기화
    nexts = [[] for _ in range(N+1)]   # 다음에 지을 수 있는 건물들의 리스트를 초기화
    dp = [0] * (N+1)   # 각 건물까지 걸린 건설 시간을 0으로 초기화

    # 건물들의 순서 저장
    for _ in range(K):
        s, e = map(int, input().split())
        nexts[s].append(e)   # 다음에 지을 수 있는 건물을 추가
        reqs[e] += 1   # 지을 수 있는 건물에 필요 건물 1개 늘린다

    # 시작건물 계산
    q = []
    for i in range(1, N+1):
        if reqs[i] == 0:   # 필요한 건물이 없는 경우(시작건물)
            q.append(i)   # 큐에 추가
            dp[i] = times[i]   # 그 건물을 짓는 시간을 더해준다

    # 이어서 건설
    while q:
        now = q.pop()   # 큐에서 하나 pop한다
        for nxt in nexts[now]:   # 해당 건물 다음 건설할 수 있는 건물별로
            reqs[nxt] -= 1   # 해당 건물을 지을 때 필요한 건물 수 1개 감소
            dp[nxt] = max(dp[now] + times[nxt], dp[nxt])   # 해당 건물까지 필요 시간을 기존과 이전시간 + 현재시간 중 큰 것으로 저장
            if not reqs[nxt]:   # 필요한 건물들이 모두 지어졌으면
                q.append(nxt)   # 큐에 추가

    # 목표 건물까지 필요한 시간 출력
    print(dp[int(input())])
