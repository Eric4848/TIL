T = int(input())
for tc in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answers = [[] for _ in range(N)]
    for r in range(N):
        for i in range(N):
            answers[r] += str(nums[N-1-i][r])
        answers[r] += ' '
        for i in range(N):
            answers[r] += str(nums[N-1-r][N-1-i])
        answers[r] += ' '
        for i in range(N):
            answers[r] += str(nums[i][N-1-r])
    print(f'#{tc+1}')
    for answer in answers:
        print(''.join(answer))
