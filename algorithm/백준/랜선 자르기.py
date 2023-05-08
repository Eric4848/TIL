K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)
while start <= end:
    mid = (start+end)//2
    cuts = [(i//mid) for i in lines]
    if sum(cuts) < N:
        end = mid - 1
    elif sum(cuts) >= N:
        start = mid + 1
print(end)

# K, N = map(int, input().split())
# lines = [int(input()) for _ in range(K)]
# total = sum(lines)
# div = total//N
#
# while True:
#     counts = 0
#     for line in lines:
#         counts += line // div
#
#     if counts == N:
#         print(div)
#         break
#
#     div -= 1
