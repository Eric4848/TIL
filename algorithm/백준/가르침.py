# 시간 초과
import sys
from itertools import permutations

input = sys.stdin.readline
N, K = map(int, input().split())
basic = ['\n', 'a', 'n', 't', 'c', 'i']
words = []
able = K-5
if able < 0:
    print(0)
else:
    answer = 0
    chk = set()
    for _ in range(N):
        word = set(input())
        for base in basic:
            word.remove(base)
        words.append(word)
    for word in words:
        if able < len(word):
            words.remove(word)
        else:
            for alph in word:
                chk.add(alph)
    for perm in permutations(chk, able):
        temp = 0
        for word in words:
            flag = 1
            for alph in word:
                if alph not in perm:
                    flag = 0
                    break
            temp += flag
        answer = max(answer, temp)
    print(answer)


# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# basic = ['a', 'n', 't', 'c', 'i']
# words = []
# able = K-5
# if able < 0:
#     print(0)
# else:
#     answer = 0
#     chk = set()
#     for _ in range(N):
#         word = input()
#         word = word[4:-4]
#         for i in range(len(word)-1, -1, -1):
#             if word[i] in basic:
#                 word = word[:i] + word[i+1:]
#         words.append(set(word))
#     for word in words:
#         if able < len(word):
#             words.remove(word)
#         else:
#             for alph in word:
#                 chk.add(alph)
#     for perm in permutations(chk, able):
#         temp = 0
#         for word in words:
#             flag = 1
#             for alph in word:
#                 if alph not in perm:
#                     flag = 0
#                     break
#             temp += flag
#         answer = max(answer, temp)
#     print(answer)
