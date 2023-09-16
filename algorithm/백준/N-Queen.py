# 시간초과 - 파이썬 문제
N = int(input())
# T/F를 사용 시 이전에 T를 F로 바꾸는 문제 발생
# matrix = [[False] * N for _ in range(N)]
# 해결하기 위해 숫자로 변경
matrix = [[0] * N for _ in range(N)]   # 체스판의 각 칸마다 0으로 초기화 한다
answer = [0]   # 정답을 0으로 초기화 한다


def dfs(r):
    if r == N:   # 각 줄마다 1개씩 놓아야 하므로 N+1번째까지 오면 배치 완료
        answer[0] += 1
        return

    for c in range(N):   # 줄별 칸마다
        if not matrix[r][c]:   # 퀸의 공격경로가 아니라면
            # T/F 사용 시 이미 T였던 곳을 처리할 수 없다
            # print(str(r)+str(c) + '-1')
            # print(matrix)
            # left = c
            # right = c
            # for i in range(r, N):
            #     matrix[i][c] = True
            #     if 0 <= left < c:
            #         matrix[i][left] = True
            #     if c <= right < N:
            #         matrix[i][right] = True
            #     left -= 1
            #     right += 1
            # dfs(r+1)
            # left = c
            # right = c
            # for i in range(r, N):
            #     matrix[i][c] = False
            #     if 0 <= left < c:
            #         matrix[i][left] = False
            #     if c <= right < N:
            #         matrix[i][right] = False
            #     left -= 1
            #     right += 1
            # print(str(r)+str(c)+'-2')
            # print(matrix)

            for i in range(1, N-r):   # 다음줄 부터 마지막줄까지
                matrix[r+i][c] += 1   # 현재 위치를 1 더해주고
                if 0 <= c-i:   # 좌측 범위 내라면
                    matrix[r+i][c-i] += 1   # 내려간 줄 수 만큼 왼쪽 칸도 1 더해준다
                if c+i < N:   # 우측도 마찬가지
                    matrix[r+i][c+i] += 1
            dfs(r+1)   # 다음줄 진행
            for i in range(1, N-r):   # 더할 때의 반대
                matrix[r+i][c] -= 1
                if 0 <= c-i:
                    matrix[r+i][c-i] -= 1
                if c+i < N:
                    matrix[r+i][c+i] -= 1


dfs(0)

print(answer)
