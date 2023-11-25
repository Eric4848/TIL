n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
answers = []   # 그림들의 크기를 저장할 정답 리스트
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(n):
    for c in range(m):
        if paper[r][c] == 1:   # 그림인 부분이면
            cnt = 1   # 크기를 1로 설정
            paper[r][c] = 0   # 해당 위치를 0으로 변경(세었다는 표시)
            q = [(r, c)]   # 큐에 위치 저장
            while q:
                R, C = q.pop()   # 그림인 부분
                for i in range(4):   # 4방항 별로
                    nr = R + dr[i]
                    nc = C + dc[i]
                    if 0 <= nr < n and 0 <= nc < m:   # 범위 이내고
                        if paper[nr][nc]:   # 세지 않은 그림이라면
                            cnt += 1   # 그림 크기를 1 증가
                            paper[nr][nc] = 0   # 해당 위치를 0으로 변경
                            q.append((nr, nc))    # 해당 위치를 큐에 추가
            answers.append(cnt)   # 전부 세었다면 정답에 추가

print(len(answers))   # 그림의 갯수를 출력
if answers:   # 그림이 있다면
    print(max(answers))   # 최댓값 출력
else:   # 없다면
    print(0)   # 0 출력
