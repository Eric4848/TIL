import heapq   # 작은 수 2개씩 더해나가야 하므로 heap을 사용

N = int(input())
nums = []   # 숫자 카드 묶음을 저장할 리스트
searched = 0   # 이미 확인 한 횟수를 0으로 초기화
for _ in range(N):
    heapq.heappush(nums, int(input()))

if N == 1:   # 정렬된 숫자들이므로 한 묶음만일때는 찾을 필요가 없다
    print(0)

else:
    for _ in range(N - 2):   # 숫자가 2개 남을때까지 == 총 묶음수보다 2번 적게 더한다
        a = heapq.heappop(nums)   # 가장 적은 묶음
        b = heapq.heappop(nums)   # 그 다음 적은 묶음
        added = a + b   # 두 묶음을 합친다
        searched += added   # 합친 수만큼 확인 횟수에 추가한다
        heapq.heappush(nums, added)   # 합친 묶음을 다시 힙에 넣어준다
    print(sum(nums) + searched)   # 두묶음만 남았을 때 두 묶음을 합치고 여태까지 확인한 횟수를 더해서 출력한다


# 오답
# import heapq
#
# N = int(input())
# nums = []
# answer = 0
# for _ in range(N):
#     heapq.heappush(nums, int(input()))
# 정렬된 숫자라는 조건이 있으므로 N == 1일때는 찾을 필요가 없다
# for _ in range(N - 2):
#     a = heapq.heappop(nums)
#     b = heapq.heappop(nums)
#     added = a + b
#     answer += added
#     heapq.heappush(nums, added)
# print(sum(nums) + answer)


# 오답
# import heapq
#
# N = int(input())
# nums = []
# answer = 0
# for _ in range(N):
#     heapq.heappush(nums, int(input()))
# if N <= 2:
#     print(sum(nums))
# else:
#     for _ in range(N-2):
#         a = heapq.heappop(nums)
#         b = heapq.heappop(nums)
#         added = a + b
#         answer += added
#         heapq.heappush(nums, added)
#     print(sum(nums) + added)   # added가 아닌 answer를 더해야한다
