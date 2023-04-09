T = int(input())
counts = [0, 1, 2, 4]
for i in range(4, 12):
    counts.append(counts[i-1] + counts[i-2] + counts[i-3])
for _ in range(T):
    num = int(input())
    print(counts[num])
