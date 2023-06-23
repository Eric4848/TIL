import sys

for _ in range(int(input())):
    S, E = map(int, sys.stdin.readline().split())
    total = E-S
    step = 1
    answer = 0
    while 0 < total:
        total -= step * 2
        answer += 2
        if total <= -step:
            answer -= 1
            break
        step += 1
    print(answer)
