import heapq

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
number = 1   # 테스트 케이스 숫자를 1로 초기화
while True:
    N = int(input())
    if N == 0:   # 입력이 0이면
        break   # 종료

    rupees = [list(map(int, input().split())) for _ in range(N)]   # 도둑루피들의 리스트
    answers = [[float('inf')] * N for _ in range(N)]   # 정답 리스트를 무한으로 초기화
    q = []   # 힙으로 저장할 큐 생성
    heapq.heappush(q, (rupees[0][0], 0, 0))   # 큐에 힙으로 시작 지점의 도둑루피 값과 시작 위치를 저장
    while q:   # 큐가 있으면
        minus, r, c = heapq.heappop(q)   # 총 마이너스되는 값과 위치를 불러온다
        if r == c == N-1:   # 현재 위치가 도착지라면
            print(f'Problem {number}: {answers[N-1][N-1]}')   # 테스트 케이스 번호와 정답을 출력하고
            number += 1   # 테스트 케이스 번호를 1 늘려주고
            break   # 종료

        for i in range(4):   # 4방면으로
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:   # 범위 내라면
                nminus = minus + rupees[nr][nc]   # 새 위치의 새로운 차감액을 구한다

                if nminus < answers[nr][nc]:   # 새로운 차감액이 새 위치의 값보다 작다면
                    answers[nr][nc] = nminus   # 값을 갱신하고
                    heapq.heappush(q, (nminus, nr, nc))   # 큐에 새 차감액과 새 위치를 저장한다


# 오답
# while True:
#     N = int(input())
#     if N == 0:
#         break
#
#     rupees = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(1, N):
#         rupees[i][0] += rupees[i-1][0]
#         rupees[0][i] += rupees[0][i-1]
#     for r in range(1, N):
#         for c in range(1, N):
#             rupees[r][c] += min(rupees[r-1][c], rupees[r][c-1])
#     print(rupees[N-1][N-1])
