H, W = map(int, input().split())
blocks = [[0] * W for _ in range(H)]   # 블럭들을 크기에 맞춰 0으로 초기화
heights = list(map(int, input().split()))
answer = 0   # 정답을 0으로 초기화

# 블록 쌓기
for i, height in enumerate(heights):   # 각 행별로 높이를 가지고
    for j in range(height):   # 높이만큼
        blocks[H-1-j][i] = 1   # 해당 행에 아래부터 쌓아준다

# 빗물 계산
for r in range(H):   # 위에서 부터
    for c in range(W):   # 가로로
        if blocks[r][c]:   # 블록이 있으면
            for i in range(c+1, W):   # 같은 높이의 다음칸들중에
                if blocks[r][i]:   # 블록으로 막힌곳이 있으면
                    answer += i - c - 1   # 정답에 그 사이 빈칸만큼 채운다
                    break   # 종료(다음에도 계속 블록이 있는 경우 때문)

print(answer)
