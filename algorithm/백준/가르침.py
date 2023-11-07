import sys
from itertools import combinations

input = sys.stdin.readline


def word2bit(word):
    bit = 0   # 알파벳을 저장할 비트를 0으로 초기화
    for char in word:   # 단어마다 알파벳 별로
        bit = bit | (1 << ord(char) - ord('a'))   # 그 알파벳의 번호수 만큼 비트를 늘려 기존과 합연산
    return bit   # 연산한 비트를 반환


N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))   # 단어별 비트 / 단어별로 map함수를 사용하여 word2bit함수 적용
base_bit = word2bit('antic')   # 반드시 사용되는 5알파벳을 base_bit로 저장

if K < 5:   # 배울 수 있는 알파벳이 5개 미만이면
    print(0)   # 0을 출력한다
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]   # 배울 수 있는 알파벳은 반드시 배워야하는 알파벳이 아닌 경우만 1로 저장한다
    answer = 0   # 정답을 0으로 초기화 한다
    for combination in combinations(alphabet, K-5):   # 조합을 활용해 반드시 배워야 할 알파벳 외의 알파벳 중 배울 수 있는 만큼 뽑아서
        know_bit = sum(combination) | base_bit   # 배운 알파벳은 조합으로 배운 것 + 반드시 알아야 하는 것으로 저장한다
        count = 0   # 배운 것으로 읽을 수 있는 단어수를 0으로 초기화한다
        for bit in bits:   # 단어별로
            if bit & know_bit == bit:   # 그 단어에 사용된 알파벳들을 모두 배웠다면(곱연산으로 안배운 것은 원본과 다르다)
                count += 1   # 읽을 수 있는 단어를 1개 늘려준다
        answer = max(answer, count)   # 정답과 읽을 수 있는 단어를 비교하여 더 큰값을 저장한다
    print(answer)

# 시간 초과
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# basic = ['\n', 'a', 'n', 't', 'c', 'i']
# words = []
# able = K-5
# if able < 0:
#     print(0)
# else:
#     answer = 0
#     chk = set()
#     for _ in range(N):
#         word = set(input())
#         for base in basic:
#             word.remove(base)
#         words.append(word)
#     for word in words:
#         if able < len(word):
#             words.remove(word)
#         else:
#             for alph in word:
#                 chk.add(alph)
#     for comb in combinations(chk, able):
#         temp = 0
#         for word in words:
#             flag = 1
#             for alph in word:
#                 if alph not in comb:
#                     flag = 0
#                     break
#             temp += flag
#         answer = max(answer, temp)
#     print(answer)


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
