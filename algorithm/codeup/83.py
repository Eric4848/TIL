r, g, b = map(int, input().split())
total = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            total += 1
print(total)
