import sys

input = sys.stdin.readline
N = int(input())
T = int(input())
pictures = [[], []]   # 걸려있는 사진과 투표수를 담을 리스트
votes = list(map(int, input().split()))
# 투표내용별로 계산
for vote in votes:
    if vote in pictures[0]:   # 이미 사진이 걸려있는 후보라면
        for i in range(N):   # 액자들을 확인하며
            if pictures[0][i] == vote:   # 해당 후보위치의
                pictures[1][i] += 1   # 투표수를 1 늘려준다

    elif len(pictures[0]) < N:   # 걸려있지 않고 남은 자리가 있다면
        pictures[0].append(vote)   # 해당 후보를 걸고
        pictures[1].append(1)   # 투표 수 1을 추가한다

    else:   # 자리가 없는 새로운 후보라면
        minimum = T   # 최소 투표수를 총 투표수로 초기화
        for i in range(N-1, -1, -1):   # 사진이 걸린 역순으로(동투표시 오래된 후보부터 제거하기 때문)
            if pictures[1][i] <= minimum:   # 최소 투표수보다 작거나 같다면
                minimum = pictures[1][i]   # 최소 투표수를 변경하고
                delete = i   # 제거할 위치를 저장
        # 사진과 투표수의 제거위치를 제거하고 새로운 사진과 투표수를 추가한다
        pictures[0] = pictures[0][0:delete] + pictures[0][delete+1:] + [vote]
        pictures[1] = pictures[1][0:delete] + pictures[1][delete+1:] + [1]

print(*sorted(pictures[0]))
