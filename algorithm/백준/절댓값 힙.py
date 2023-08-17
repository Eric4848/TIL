import heapq
import sys

input = sys.stdin.readline   # 사용하지 않으면 시간 초과

plus = []   # 양수를 저장할 힙
minus = []   # 음수를 저장할 힙
N = int(input())
for _ in range(N):   # 반복 횟수만큼
    num = int(input())
    if num == 0:   # 입력이 0인 경우
        if not plus and not minus:   # 양수, 음수 모두 숫자가 없으면
            print(0)   # 0을 출력하고

        elif not minus:   # 음수가 없으면
            print(heapq.heappop(plus))   # 양수에서 pop하여 출력하고

        elif not plus:   # 양수가 없으면
            print(-heapq.heappop(minus))   # 음수에서 pop하여 출력하고

        else:   # 둘 다 있으면
            pos = heapq.heappop(plus)   # 양수
            neg = heapq.heappop(minus)   # 음수 각각 pop하여

            if neg <= pos:   # 음수의 절댓값이 더 작은경우
                print(-neg)   # 음수로 만들어주어 출력하고
                heapq.heappush(plus, pos)   # pop했던 양수는 다시 push해준다
            else:   # 반대의 경우 마찬가지이다
                print(pos)
                heapq.heappush(minus, neg)

    elif 0 < num:   # 입력이 양수인 경우
        heapq.heappush(plus, num)   # 양수 힙에 넣어준다

    else:   # 입력이 음수인 경우
        heapq.heappush(minus, -num)   # -를 붙여 음수 힙에 넣어준다
