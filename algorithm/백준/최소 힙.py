import sys
import heapq   # heap을 사용하기 위해 추가 / heap은 이진트리로 작은것에서 큰것 순으로 정렬
input = sys.stdin.readline   # readline을 사용해야 시간초과 나지 않음
N = int(input())
nums = []   # heap을 저장할 리스트
for _ in range(N):
    num = int(input())
    if num == 0:
        if nums:   # heap에 저장된 값이 있으면
            print(heapq.heappop(nums))   # 가장 작은 수를 pop하여 출력해준다 (heappop 시 가장 작은 수 출력)
        else:
            print(0)
    else:
        heapq.heappush(nums, num)   # 0이 아닌경우 heap에 그 숫자를 추가해 준다
