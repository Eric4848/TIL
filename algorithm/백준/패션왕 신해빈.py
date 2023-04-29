T = int(input())
for _ in range(T):
    n = int(input())
    kinds = {}
    for _ in range(n):
        _, kind = input().split()
        if kind in kinds.keys():
            kinds[kind] += 1
        else:
            kinds[kind] = 1

    if len(kinds.keys()) == 1:
        for val in kinds.values():
            print(val)
    else:
        answer = 1
        for val in kinds.values():
            answer *= (val + 1)
        answer -= 1
        print(answer)
