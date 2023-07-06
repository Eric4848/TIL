import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))   # 숫자들을 입력받는다, [0]은 계산을 위해 추가해준다
for i in range(N):   # N-1까지
    nums[i+1] += nums[i]   # 이전 숫자를 더해준다
for _ in range(M):
    s, e = map(int, input().split())
    print(nums[e] - nums[s-1])   # 끝나는 숫자 위치에서 시작위치보다 하나 앞 위치의 숫자를 빼준다
