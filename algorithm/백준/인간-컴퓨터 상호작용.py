import sys

input = sys.stdin.readline
word = input().rstrip()   # rstrip으로 알파벳별로 쪼갠다
counts = [[0] * 26]   # 알파벳별 갯수를 0개로 초기화(나중의 값에서 빼기 위해 0으로 초기화)
for i, alph in enumerate(word):   # enumerate로 알파벳 위치와 알파벳별로
    counts.append(counts[-1][:])   # 이전 내용을 복사해 붙여넣고
    counts[i+1][ord(alph) - 97] += 1   # 마지막 칸에서 알파벳 위치에 1 추가

for _ in range(int(input())):
    alph, s, e = input().split()
    alph = ord(alph) - 97   # 알파벳 을 인덱스위치에 맞춰준다
    s = int(s)
    e = int(e)
    print(counts[e + 1][alph] - counts[s][alph])   # 조건 맨 뒤의 갯수 - 조건 맨 앞의 갯수를 출력한다


# 50
# import sys
#
# input = sys.stdin.readline
# word = input()
# alphs = {}
# for i in range(len(word)):
#     if word[i] in alphs.keys():
#         alphs[word[i]].append(i)
#     else:
#         alphs[word[i]] = [i]
#
# for _ in range(int(input())):
#     alph, s, e = input().split()
#     s = int(s)
#     e = int(e)
#     if alph in alphs.keys():
#         answer = 0
#         for i in alphs[alph]:
#             if e < i:
#                 break
#             elif s <= i:
#                 answer += 1
#         print(answer)
#
#     else:
#         print(0)


# 50
# word = input()
# alphs = {i: word[i] for i in range(len(word))}
# for _ in range(int(input())):
#     alph, s, e = input().split()
#     answer = 0
#     for i in range(int(s), int(e) + 1):
#         if alphs[i] == alph:
#             answer += 1
#     print(answer)

# 50
# word = input()
# for _ in range(int(input())):
#     alph, s, e = input().split()
#     answer = 0
#     for i in range(int(s), int(e)+1):
#         if word[i] == alph:
#             answer += 1
#     print(answer)
