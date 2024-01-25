import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
min_cut = 0   # 자르는 최소 높이
max_cut = max(trees)   # 자르는 최대 높이

while min_cut <= max_cut:
    cut = (min_cut + max_cut) // 2   # 자르는 높이를 평균으로 설정
    have = 0   # 가져갈 수 있는 나무 길이를 초기화
    for tree in trees:   # 나무별로
        if 0 < tree - cut:   # 자르고 남는 부분이 있다면
            have += tree - cut   # 추가
            if M <= have:   # 필요한 길이만큼 모았으면
                break   # 계산을 멈춰도 된다

    if M <= have:   # 가지고 있는 부분이 더 크다면
        min_cut = cut + 1   # 최소치를 현재 + 1로 변경하고
        answer = cut   # 현재 길이를 정답에 저장한다
    else:   # 아닌 경우
        max_cut = cut - 1   # 최대치를 현재 - 1로 변경한다

print(answer)
