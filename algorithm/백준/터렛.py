T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5

    maxr = max(r1, r2)
    minr = min(r1, r2)

    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    elif d < maxr:
        if d + minr > maxr:
            print(2)
        elif d + minr == maxr:
            print(1)
        else:
            print(0)

    else:
        if r1 + r2 == d:
            print(1)
        elif minr + maxr < d:
            print(0)
        else:
            print(2)
