import sys

input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split())))   # 숫자카드들을 정렬하여 저장

M = int(input())
nums = list(map(int, input().split()))

answers = []   # 정답을 담을 리스트

for num in nums:   # 확인 할 숫자별로
    min_card = 0   # 최소 인덱스
    max_card = N - 1   # 최대 인덱스
    answer = 0   # 카드중에 없다고 설정
    # 인덱스를 이분 탐색
    while min_card <= max_card:
        card = (min_card + max_card) // 2

        if num < cards[card]:   # 찾는 숫자보다 해당 카드 숫자가 크면
            max_card = card - 1   # 최대 인덱스 줄임

        elif cards[card] < num:   # 찾는 숫자보다 해당 카드 숫자가 작으면
            min_card = card + 1   # 최소 인덱스 늘림

        else:   # 찾는 숫자라면
            answer = 1   # 카드중에 있다고 바꾸고
            break   # 종료

    answers.append(answer)   # 유무여부 저장

print(*answers)
