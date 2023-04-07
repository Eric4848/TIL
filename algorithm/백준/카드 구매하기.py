n = int(input())
data = [0] + list(map(int, input().split()))
D = data[:]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        D[i] = min(D[i], D[i - j] + data[j])

print(D[n])

# num = int(input())
# values = [0] + list(map(int, input().split()))
# minimum = float('inf')
#
# for n, cost in enumerate(values):
#     if n == 0:
#         continue
#     if num % n != 0:
#         continue
#     total = (num / n) * cost
#     if total < minimum:
#         minimum = total
#
# print(int(minimum))
