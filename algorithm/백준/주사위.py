N = int(input())
# 주사위가 하나인 경우
if N == 1:
    nums = sorted(list(map(int, input().split())))
    print(sum(nums[0:5]))   # 가장 큰 수를 제외한 나머지 숫자의 합을 출력
# 2개 이상인 경우
else:
    a, b, c, d, e, f = map(int, input().split())
    nums = sorted([min(a, f), min(b, e), min(c, d)])   # 마주보는 면끼리 둘 중 작은 숫자를 정렬한다
    answer = 0   # 정답을 0으로 초기화한다
    # 5면에 보이는 부분을 계산한다(N * N 5면 - 모서리 N * 8개 + 귀퉁이 4개) * 가장 숫자
    answer += (5 * N * N - 8 * N + 4) * nums[0]
    # 모서리 부분을 계산(8 모서리 * N - 4 * 2[귀퉁이가 2번 겹침]) * 두번째로 작은 숫자
    answer += (N-1) * 8 * nums[1]
    # 귀퉁이 계산(4개) * 가장 큰 숫자
    answer += 4 * nums[2]

    print(answer)
