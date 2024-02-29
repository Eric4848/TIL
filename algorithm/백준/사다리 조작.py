import sys

input = sys.stdin.readline
N, M, H = map(int, input().split())
ladders = [[0] * N for _ in range(H)]   # 사다리를 가로 선 없다는 0으로 초기화
answer = 4   # 정답을 최대 설치 갯수 + 1인 4로 초기화

# 사다리 계산
for _ in range(M):
    h, l = map(int, input().split())   # 설치 높이랑 설치할 사다리 위치
    ladders[h-1][l] = -1   # 해당 높이에 우측은 -1로
    ladders[h-1][l-1] = 1   # 해당 높이에 좌측은 1로


# 전부 돌아가는지 확인하는 함수
def chk():
    for s in range(N):   # 각 시작위치별로
        now = s   # 현재 사다리 위치를 시작위치로 설정
        for h in range(H):   # 높이를 내려가며(이동 후 재이동은 불가능)
            if ladders[h][now]:   # 사다리가 이어져있다면
                now += ladders[h][now]   # 해당 방향으로 이동
        if now != s:   # 다 내려왓을 때 원위치가 아니라면
            return False   # 거짓 반환
    return True   # 전부 원위치인 경우 진실 반환


# 사다리 추가하는 함수
def calc(cnt, r, c):   # 추가한 사다리 수, 높이, 사다리 위치
    global answer

    # 현재까지 추가한 사다리가 정답과 같은 경우
    if answer == cnt:
        return

    # 전부 돌아가는지 확인
    if chk():
        answer = min(answer, cnt)
        return

    # 이미 3개의 사다리를 놓은경우
    if cnt == 3:
        return

    # 사다리 추가
    for i in range(r, H):
        if i == r:   # 입력 높이인 경우
            now = c   # 입력 사다리부터
        else:   # 다음부턴
            now = 0   # 처음부터

        # 사다리별로 추가
        for j in range(now, N-1):   # 기준부터 맨마지막 전 사다리까지
            if not ladders[i][j] and not ladders[i][j+1]:   # 현재와 다음 사다리에 연결된 중간다리가 없다면
                # 중간다리 추가
                ladders[i][j] = 1
                ladders[i][j+1] = -1
                # 다음으로 계산(사다리를 두면 다음에는 둘 수 없으므로 +2)
                calc(cnt+1, i, j+2)
                # 중간다리 제거
                ladders[i][j] = 0
                ladders[i][j+1] = 0


calc(0, 0, 0)
# 불가능한 경우
if answer == 4:
    answer = -1
print(answer)
