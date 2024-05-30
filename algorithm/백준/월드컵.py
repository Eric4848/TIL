from itertools import combinations

answer = []   # 정답을 담을 리스트
games = list(combinations(range(6), 2))   # 경기 매칭을 리스트로 저장


# 경기 진행 함수
def dfs(n):
    global prob
    if n == 15:   # 15번째 경기까지 진행했다면
        prob = 1   # 가능
        return
    # 경기 진행
    p1, p2 = games[n]   # 두 경기를 진행할 번호
    for i in range(3):   # p1이 승, 무, 패 3경우
        if tables[p1][i] and tables[p2][2-i]:   # 승, 무, 패 / 패, 무, 승 이 각각 있다면
            tables[p1][i] -= 1   # 1개씩
            tables[p2][2-i] -= 1   # 줄여주고
            dfs(n+1)   # 다음 진행
            tables[p1][i] += 1   # 원래대로
            tables[p2][2-i] += 1   # 복구


for _ in range(4):
    chk = 1   # 각각 5번씩 경기함
    results = list(map(int, input().split()))
    tables = [results[i:i+3] for i in range(0, 18, 3)]   # 3개씩 잘라 저장(승, 무, 패)
    for t in tables:   # 각 나라별로
        if sum(t) != 5:   # 5회 경기가 아닌경우
            chk = 0   # 경기 수 이상
    prob = 0   # 가능 여부 초기화
    if chk:   # 경기 수가 정상이라면
        dfs(0)   # 경기 진행
    answer.append(prob)   # 가능 여부 저장
print(*answer)
