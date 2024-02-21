from collections import deque

N, K = map(int, input().split())
belts = deque(list(map(int, input().split())))   # 벨트의 내구도를 deque에 저장(이동을 편하게 계산하기 위해)
robots = deque([False] * N)   # 로봇들의 위치를 deque에저장
answer = 0


# 계산할 함수
def sol():
    global answer
    while True:
        answer += 1   # 단계 + 1

        # 1
        belts.appendleft(belts.pop())   # 벨트 한칸씩 이동
        robots.appendleft(robots.pop())   # 로봇 한칸씩 이동
        robots[-1] = False   # 내리는 칸의 로봇을 내린다

        # 2
        for i in range(N-2, -1, -1):   # 윗쪽 벨트 의 내리는 칸 전부터 올리는 칸 까지
            if robots[i]:   # 로봇이 있으면
                if not robots[i+1] and belts[i+1]:   # 다음 칸에 로봇이 없고, 그 칸에 내구도가 있다면
                    robots[i+1] = True   # 로봇 위치를
                    robots[i] = False   # 옮겨주고
                    belts[i+1] -= 1   # 벨트 내구도를 1 줄인다
        robots[-1] = False   # 내리는 칸의 로봇을 내린다

        # 3
        if not robots[0] and belts[0]:   # 올리는 칸에 로봇이 없고 내구도가 있으면
            robots[0] = True   # 로봇을 올리고
            belts[0] -= 1   # 내구도를 내린다

        # 4
        cnt = 0   # 내구도가 없는 벨트 초기화
        for i in range(2 * N):   # 전체 벨트 칸마다
            if not belts[i]:   # 내구도가 없으면
                cnt += 1   # 내구도가 없는 칸을 1개 추가
                if K == cnt:   # 내구도가 없는 조건과 같아지면
                    return answer   # 정답 반환


print(sol())
