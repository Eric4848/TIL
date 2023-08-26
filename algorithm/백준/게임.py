# int(Y / X * 100)을 사용하면 틀린다
X, Y = map(int, input().split())
Z = (Y*100) // X

if 99 <= Z:   # 현재 승률이 99% 이상이라면 100%로 만들 수 업다
    print(-1)

else:   # 이진탐색
    A = 1   # 시작점
    B = X   # 끝점
    answer = 0   # 정답
    while A <= B:
        mid = (A+B) // 2   # 이진분류를 위한 중간값
        if ((Y+mid)*100) // (X+mid) == Z:   # 중간값을 더한 후 승률의 변화가 없다면
            A = mid + 1   # 시작점을 이동시킨다
        else:   # 승률의 변화가 있다면
            answer = mid   # 정답에 더해준 중간값을 넣어주고
            B = mid - 1   # 끝점을 이동시킨다
    print(answer)


# 시간초과
# X, Y = map(int, input().split())
# if X == Y:
#     print(-1)
# else:
#     Z = int(Y / X * 100)
#     for i in range(1, X):
#         new = int((Y+i) / (X+i) * 100)
#         if Z != new:
#             print(i)
#             break
