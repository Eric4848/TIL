n = int(input())
nums = list(map(int, input().split()))
calcs = list(map(int, input().split()))   # 연산자 갯수 리스트
answer = [float('-inf'), float('inf')]   # 최대, 최솟값 초기화


def search(result, counts):
    if counts == n:   # 모든 연산이 끝나면
        if result > answer[0]:
            answer[0] = result
        if result < answer[1]:
            answer[1] = result
        return

    if calcs[0] != 0:   # 덧셈 연산자가 남아있으면
        calcs[0] -= 1   # 연산자 갯수를 1개 줄이고
        search(result + nums[counts], counts + 1)   # 결과에 계산한 값을 넣고 counts를 1 증가시킨다
        calcs[0] += 1   # 연산자 갯수를 다시 돌려준다

    if calcs[1] != 0:   # 뺄셈 연산자가 남아있으면
        calcs[1] -= 1   # 연산자 갯수를 1개 줄이고
        search(result - nums[counts], counts + 1)   # 결과에 계산한 값을 넣고 counts를 1 증가시킨다
        calcs[1] += 1   # 연산자 갯수를 다시 돌려준다

    if calcs[2] != 0:   # 곱셈 연산자가 남아있으면
        calcs[2] -= 1   # 연산자 갯수를 1개 줄이고
        search(result * nums[counts], counts + 1)   # 결과에 계산한 값을 넣고 counts를 1 증가시킨다
        calcs[2] += 1   # 연산자 갯수를 다시 돌려준다

    if calcs[3] != 0:   # 나눗셈 연산자가 남아있으면
        calcs[3] -= 1   # 연산자 갯수를 1개 줄이고
        search(int(result / nums[counts]), counts + 1)   # 결과에 계산한 값의 몫부분을 넣고 counts를 1 증가시킨다
        # //의 경우 음수일 때 나머지를 음수로 두지 않기 위해 결과에 1을 빼기 때문에 int사용
        calcs[3] += 1   # 연산자 갯수를 다시 돌려준다


search(nums[0], 1)   # 결과를 첫번째 숫자로 주고 counts를 1부터 시작(연산할 숫자의 자리)
print(int(answer[0]))
print(int(answer[1]))
