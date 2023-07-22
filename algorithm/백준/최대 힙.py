import sys
import heapq
input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if nums:
            print(-heapq.heappop(nums))   # 최소 힙과 같지만 heap은 sort를 사용할 수 없어 -로 저장하여 역순을 취해준다
        else:
            print(0)
    else:
        heapq.heappush(nums, -num)   # 저장할 때 -를 붙여 저장하여 절댓값이 내림차순이 되도록 저장한다
