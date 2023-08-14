N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()   # 용액을 정렬한다

minimum = abs(liquids[0] + liquids[N-1])   # 합한 용액의 최소 차이를 저장한다
answer = [liquids[0], liquids[N-1]]   # 정답에 첫 용애과 마지막 용액을 저장한다

left = 0   # 작은 숫자부터 점점 커지는 부분
right = N - 1   # 큰 숫자부터 점점 작아지는 부분

while left != right:   # 선택된 용액이 같아질때까지
    mixed = liquids[left] + liquids[right]   # 섞은 용액은 두 위치의 용액의 합이다

    if abs(mixed) < minimum:   # 섞은 용액이 원래보다 0에 가까우면
        minimum = abs(mixed)   # 값을
        answer = [liquids[left], liquids[right]]   # 저장해준다
        if answer == 0:   # 그 값이 0이면
            break   # 정지한다

    if mixed < 0:   # 혼합한 값이 음수면
        left += 1   # 좌측을 하나 키우고
    else:   # 양수면
        right -= 1   # 우측을 하나 줄인다

print(answer[0], answer[1])

# N = int(input())
# liquids = list(map(int, input().split()))
# minimum = [float('inf'), float('inf')]
# liquids.sort()
# answer = [abs(liquids[0] + liquids[-1]), [0, N-1]]
# for _ in range(N-1):
#     if abs(liquids[answer[1][0]]) < abs(liquids[answer[1][1]]):
#         if abs(liquids[answer[1][0]] + liquids[answer[1][1] - 1]) < answer[0]:
#             answer[1][1] = answer[1][1] - 1
#             answer[0] = abs(liquids[answer[1][0]] + liquids[answer[1][1] - 1])
#     else:
#         if abs(liquids[answer[1][0] + 1] + liquids[answer[1][1]]) < answer[0]:
#             answer[1][0] = answer[1][0] + 1
#             answer[0] = abs(liquids[answer[1][0] + 1] + liquids[answer[1][1]])
# print(liquids[answer[1][0]], liquids[answer[1][1]])

# 시간초과
# N = int(input())
# liquids = list(map(int, input().split()))
# minimum = [float('inf'), float('inf')]
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             diff = abs(liquids[i] + liquids[j])
#             if diff < minimum[0]:
#                 minimum[0] = diff
#                 minimum[1] = [liquids[i], liquids[j]]
# print(minimum[1])

