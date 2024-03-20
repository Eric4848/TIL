import sys
import copy
from collections import deque
from itertools import combinations

# 열값이 증가하는 순으로 이동, 아래쪽으로는 확인할 필요 없다
dr = [0, -1, 0]
dc = [-1, 0, 1]


# 모든 웨이브가 끝난 지 확인하는 함수
def check():
    enemy = 0   # 적들의 합을 0으로 초기화
    for i in range(N):   # 행별로
        enemy += sum(case[i])   # 적들의 수를 더한다
    return enemy   # 적들의 수 반환


# 공격할 적을 찾는 함수
def aim(archer):
    q = deque([(N, archer, 0)])   # deque에 성이 있는 열, 궁수의 위치, 사거리 0을 추가한다
    # bfs 진행
    while q:
        r, c, d = q.popleft()
        # 최대 사거리까지 오면 종료(시작이 0이었으므로)
        if d == D:
            continue
        # 3방향으로 계산(아래로는 확인할 필요 없기때문)
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 이내인 경우
            if 0 <= nr < N and 0 <= nc < M:
                # 적이 있는 경우
                if case[nr][nc]:
                    return [nr, nc]   # 적 위치 반환
                # 적이 없는 경우
                else:
                    q.append((nr, nc, d+1))   # 다음 적 탐색 진행


# 웨이브를 공격하는 함수
def attack():
    kill = 0   # 죽인 적의 수를 0으로 초기화
    while True:
        targets = []   # 공격할 적의 위치를 담을 리스트
        for archer in archers:   # 궁수들의 위치별로
            if aim(archer):   # 공격할 적을 찾았다면
                targets.append(aim(archer))   # 위치를 리스트에 담는다

        for r, c in targets:   # 적의 위치 별로
            if case[r][c]:   # 적이 있다면
                kill += 1   # 죽인 적의 수를 1 늘리고
                case[r][c] = 0   # 죽임 표시를 한다

        # 적의 진격
        case.pop()   # 맨 아랫줄을 진격시키고
        case.appendleft([0 for _ in range(M)])   # 맨 윗줄에 빈 칸 추가

        # 적이 모두 죽었다면 종료
        if check() == 0:
            return kill


input = sys.stdin.readline
N, M, D = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for archers in combinations(range(M), 3):   # 궁수의 위치를 조합하여
    case = deque(copy.deepcopy(fields))   # 공격할 필트를 deque에 복사한다
    answer = max(answer, attack())   # 웨이브 공격

print(answer)
