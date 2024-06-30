T = int(input())
for tc in range(T):
    answer = -float('inf')
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    LA = len(A)
    LB = len(B)

    if LA < LB:
        d = LB - LA
        for i in range(d+1):
            tmp = 0
            for j in range(LA):
                tmp += A[j] * B[i + j]
            if answer < tmp:
                answer = tmp
    else:
        d = LA - LB
        for i in range(d+1):
            tmp = 0
            for j in range(LB):
                tmp += A[i+j] * B[j]
            if answer < tmp:
                answer = tmp

    print(f'#{tc+1} {answer}')
