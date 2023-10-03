# 시간 초과
import sys

input = sys.stdin.readline
F = input()[:-1]
S = input()[:-1]

flag = 1
while flag and F:
    for i in range(len(F)):
        if F[i] == S[0]:
            chk = 0
            for j in range(1, len(S)):
                if F[i+j] != S[j]:
                    chk = 1
                    break
            if chk:
                continue
            F = F[0:i] + F[i+len(S):]
            break
        if i == len(F)-1:
            flag = 0
if F:
    print(F)
else:
    print('FRULA')
