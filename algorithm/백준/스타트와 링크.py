import sys

n = int(sys.stdin.readline())   # *1차이점
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [False for _ in range(n)]  # 1
min_value = sys.maxsize  # 2 *2차이점


def backTracking(depth, idx):  # 3
    global min_value
    if depth == n // 2:  # 4
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:  # 5
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]:  # 6
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1 - power2))  # 7
        return

    for i in range(idx, n):  # 8
        if not visit[i]:
            visit[i] = True
            backTracking(depth + 1, i + 1)  # 9
            visit[i] = False


backTracking(0, 0)
print(min_value)

# 시간 초과
# import sys
# N = int(input())
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# answer = float('inf')   # 정답을 초기화
# team1 = [False] * N   # 첫번째 팀의 팀원
#
#
# def calc(counts, starts):   # 뽑은 인원수와 선택을 시작할 선수 번호
#     global answer
#     if counts == N / 2:   # 한팀이 꾸려지면
#         ability1, ability2 = 0, 0   # 각 팀의 능력치를 초기화
#         for i in range(N):   # 팀원이
#             for j in range(N):   # 팀원과 같이 있으면
#                 if team1[i] and team1[j]:   # team1에 있으면
#                     ability1 += matrix[i][j]   # 능력치1에 더해주고
#                 elif not team1[i] and not team1[j]:   # team1에 없으면(team2에 있으면)
#                     ability2 += matrix[i][j]   # 능력치2에 더해준다
#         answer = min(answer, abs(ability1-ability2))   # 현재 정답과 계산한 능력치 차 중에 작은 것 저장
#     for i in range(starts, N):   # 선택을 시작할 선수 부터
#         team1[i] = True   # team1에 넣어 준다
#         calc(counts+1, starts+1)   # 다음 인원선택을 한다
#         team1[i] = False   # team1에서 뺀다
#
#
# calc(0, 0)
# print(answer)
