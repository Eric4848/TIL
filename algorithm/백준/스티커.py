T = int(input())
for _ in range(T):
    n = int(input())
    stickers1 = list(map(int, input().split()))   # 첫번째 줄 저장
    stickers2 = list(map(int, input().split()))   # 두번쨰 줄 저장
    stickers1[1] += stickers2[0]   # 첫번째줄 2번째 자리에 두번째줄 1번째 숫자를 더해준다
    stickers2[1] += stickers1[0]   # 두번째줄 2번째 자리에 첫번째줄 1번째 숫자를 더해준다
    for i in range(2, n):  # 세번째 숫자부터 마지막 숫자까지
        stickers1[i] += max(stickers2[i-1], stickers2[i-2])   # 첫번째줄 n번째 숫자와 두번째줄 n-1, n-2번째 숫자중 큰것을 더해준다 (n-1을 건너 뛸지 결정)
        stickers2[i] += max(stickers1[i-1], stickers1[i-2])   # 두번째줄 n-1은 첫번째줄 n-2와 두번째줄 n-1의 합, 두번째줄 n-2는 n-1번째를 더하지 않은 값이다
    print(max(stickers1[n-1], stickers2[n-1]))


# 중간을 건너 뛰는 경우 계산 X
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     stickers1 = list(map(int, input().split()))
#     stickers2 = list(map(int, input().split()))
#     scores = [0, 0]
#     for i in range(n):
#         if i % 2 == 0:
#             scores[0] += stickers1[i]
#             scores[1] += stickers2[i]
#         else:
#             scores[0] += stickers2[i]
#             scores[1] += stickers1[i]
#     print(max(scores))
