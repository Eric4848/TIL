N = int(input())
nums = list(map(int, input().split()))
X = int(input())
nums.sort()   # 숫자들을 정렬(중복이 없기 때문)
answer = 0   # 정답의 갯수를 0으로 초기화
s = 0   # 시작 숫자(가장 작은 숫자)
e = N - 1   # 끝 숫자(가장 큰 숫자)

while s != e:   # 시작 숫자와 끝 숫자가 같아질 때까지
    added = nums[s] + nums[e]   # 각 위치의 숫자의 합
    if added == X:   # 합한 숫자가 목표 숫자와 같으면
        answer += 1   # 정답 갯수를 1개 늘린다
# 숫자들을 정렬하였기 때문에 양끝 숫자에서 한칸씩 이동하면서 진행
    if added < X:   # 합이 목표 숫자보다 작다면
        s += 1   # 처음 숫자를 다음숫자로 변경한다
    else:   # 합이 목표 숫자보다 크거나 같다면
        e -= 1   # 끝 숫자를 이전 숫자로 변경한다

print(answer)
