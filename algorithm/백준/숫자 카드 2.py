import sys

input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int, input().split())))
dict_card = {}   # 카드별 갯수를 저장할 dict
for card in cards:
    if card in dict_card.keys():   # 해당 카드가 있다면
        dict_card[card] += 1   # 카드 장수를 늘려준다
    else:   # 해당 카드가 없다면
        dict_card[card] = 1   # 해당 카드를 추가한다

M = int(input())
nums = list(map(int, input().split()))

answers = []

for num in nums:   # 확인할 숫자들 중
    if num in dict_card.keys():   # 그 카드가 있다면
        answers.append(dict_card[num])   # 가진 수만큼 저장
    else:   # 없다면
        answers.append(0)   # 0을 저장

print(*answers)


# import sys
#
# input = sys.stdin.readline
# N = int(input())
# cards = sorted(list(map(int, input().split())))
# # 숫자 카드 방식에서 dict로 카드별 숫자를 세어 출력
# dict_card = {}
# for card in cards:
#     if card in dict_card.keys():
#         dict_card[card] += 1
#     else:
#         dict_card[card] = 1
#
# M = int(input())
# nums = list(map(int, input().split()))
#
# answers = []
#
# for num in nums:
#     min_card = 0
#     max_card = N - 1
#     answer = 0
#     while min_card <= max_card:
#         card = (min_card + max_card) // 2
#
#         if num < cards[card]:
#             max_card = card - 1
#
#         elif cards[card] < num:
#             min_card = card + 1
#
#         else:
#             answer = dict_card[cards[card]]
#             break
#
#     answers.append(answer)
#
# print(*answers)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# cards = sorted(list(map(int, input().split())))
#
# M = int(input())
# nums = list(map(int, input().split()))
#
# answers = []
#
#
# def search(n, idx):
#     tmp = 0
#     if 0 <= idx+n < N and cards[idx+n] == num:
#         tmp = 1
#         tmp += search(n, idx+n)
#     return tmp
#
#
# for num in nums:
#     min_card = 0
#     max_card = N - 1
#     answer = 0
#     while min_card <= max_card:
#         card = (min_card + max_card) // 2
#
#         if num < cards[card]:
#             max_card = card - 1
#
#         elif cards[card] < num:
#             min_card = card + 1
#
#         else:
#             answer = 1
#             answer += search(1, card)
#             answer += search(-1, card)
#             break
#
#     answers.append(answer)
#
# print(*answers)
