import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    answer = 1   # 서류 1등은 항상 합격하기 때문에
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks.sort()   # 서류 등수를 기준으로 정렬하여
    maximum = ranks[0][1]   # 서류 1등의 면접 등수를 저장
    for i in range(1, N):   # 서류 2등부터
        if ranks[i][1] < maximum:   # 면접 등수가 이전의 최대 등수보다 높다면(크기가 작다면)
            answer += 1   # 합격자 수를 1명 늘리고
            maximum = ranks[i][1]   # 최대 점수를 업데이트
    print(answer)
