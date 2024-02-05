import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
# 계산을 위해 k-1개만큼 앞부분을 뒤에 추가해준다
for i in range(k-1):
    sushi.append(sushi[i])

h = 0   # 앞부분
t = k   # 뒷부분
answer = 0
for i in range(N):   # 총 초밥의 갯수만큼(시작초밥)
    tmp = set(sushi[h+i:t+i] + [c])   # 시작초밥 ~ 조건까지의 초밥 + 쿠폰초밥을 set으로 정리
    answer = max(answer, len(tmp))   # 정답과 새로운 조합 중 큰 것 저장
print(answer)


# from collections import deque
#
# N, d, k, c = map(int, input().split())
# sushi = [int(input()) for _ in range(N)]
# for i in range(k-1):
#     sushi.append(sushi[i])
#
# h = 0
# t = k
# common = 0
# tmp = deque([])
# cnt = 0
# for i in range(k):
#     if sushi[i] == c:
#         common += 1
#
#     if sushi[i] not in tmp:
#         cnt += 1
#
#     tmp.append(sushi[i])
#
# print(cnt, common, tmp)
