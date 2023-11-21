N = int(input())
nums = []   # 숫자들을 저장할 리스트
answer = 0   # 정답을 0으로 초기화

for _ in range(N):
    nums.append(int(input()))

nums.sort()   # 숫자들을 정렬한다
while nums and 0 < nums[-1]:   # 숫자가 있고 양수일 때(0인경우 음수와 곱해서 줄여야 하므로)
    num = nums.pop()   # 가장 큰 숫자를 뽑는다
    if nums and 1 < nums[-1]:   # 숫자가 있고 2보다 클 때(1은 곱하는 것 보다 1까지 더하는게 더 크다)
        num *= nums.pop()   # 다음으로 큰 숫자를 뽑아 곱해준다
    answer += num   # 숫자를 정답에 더해준다

if nums:   # 음수가 있는 경우
    nums.sort(reverse=True)   # 숫자들을 역정렬해준다
    while nums:   # 숫자들에 대해
        num = nums.pop()   # 가장 작은 수를 뽑고(음수)
        if nums:   # 숫자가 남아있다면(음수나 0)
            num *= nums.pop()   # 뽑아서 곱해준다(음수끼리 곱해 가장 큰 수)
        answer += num   # 그 값을 정답에 더해준다

print(answer)
