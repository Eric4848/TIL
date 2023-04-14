n = int(input())

totals = [1, 3]
if n > 2:
    for i in range(2, n):
        totals.append(totals[i-1] + 2 * totals[i-2])

print(totals[n-1] % 10007)
