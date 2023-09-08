from collections import deque   # 그냥 추가하면 시간 초과

N = int(input())
cnts = deque([3, 7])   # 초기값을 N1 = 3, N2 = 7을 넣어준다
if N < 3:   # 입력이 1, 2인 경우
    print(cnts[N-1])   # 초기값으로 출력
else:
    for _ in range(N-2):   # Nn = Nn-1 * 2 + Nn-2의 계산이 나온다(맨 밑줄 숫자들의 종류별 갯수)
        t = cnts.popleft()   # 계속 추가하면 메모리 초과하므로 popleft를 활용해 2개로 유지한다
        cnts.append(t + cnts[0] * 2)   # 계산에 맞게 추가한다
    print(cnts[-1] % 9901)

#              0 0
# N = 1 -> 3   0 0 / 0 1 / 1 0
# N = 2 -> 7   0 0          // 0 1     // 1 0
#              0 0 /0 1/1 0 // 0 0/1 0 // 0 0/0 1
# N = 3 -> 17  0 0 * 3 / 1 0 * 2 / 1 0 * 2   9 + 4 + 4 => 17 => N1 + N2 + N2
# N = 4 -> 41  0 0 * 7 / 1 0 * 5 / 1 0 * 5   21 + 10 + 10 => 41 N2 + N3 + N3
