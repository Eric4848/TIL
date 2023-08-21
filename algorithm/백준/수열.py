L, N = map(int, input().split())
nums = list(map(int, input().split()))
answer = [0]   # 합들을 저장할 리스트 / 처음 합을 0으로 초기화 한다
for i in range(N):
    answer[0] += nums[i]   # 맨 앞의 합숫자를 구해준다

for i in range(L - N):   # 총길이에서 더하는 숫자만큼 뺀 만큼
    now = answer.pop()   # 마지막 합을 가져와서
    answer.append(now)   # 다시 넣어주고
    now = now - nums[i] + nums[i + N]   # 그 합의 맨 앞 숫자를 빼고 맨뒤 다음 숫자를 더해준 후
    answer.append(now)   # 정답에 넣어준다

print(max(answer))
