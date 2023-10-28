N = int(input())
A = list(map(int, input().split()))
dpu = [1] * N   # 증가 부분을 저장
dpd = [1] * N   # 감소 부분을 저장
answer = 0   # 정답을 0으로 초기화
# 증가 부분 계산
for i in range(0, N):   # 뒷 숫자
    for j in range(0, i):   # 앞 숫자
        if A[j] < A[i]:   # 앞 숫자보다 뒷 숫자가 더 크면
            dpu[i] = max(dpu[i], dpu[j] + 1)   # 뒷 숫자 자리에 앞 숫자의 증가 수 + 1과 뒷 숫자의 증가 수 중 큰 것을 저장
# 감소 부분 계산
for i in range(N-1, -1, -1):   # 앞 숫자
    for j in range(N-1, i, -1):   # 뒷 숫자
        if A[j] < A[i]:   # 뒷 숫자봐 앞 숫자가 더 크면
            dpd[i] = max(dpd[i], dpd[j] + 1)   # 앞 숫자 자리에 뒷 숫자의 증가 수 + 1과 앞 숫자의 증가 수 중 큰 것을 저장
# 정답 계산
for i in range(N):
    answer = max(answer, dpu[i]+dpd[i])   # 정답과 해당 위치 증가 부분 + 감소 부분의 합 중 큰 것을 저장
print(answer - 1)   # 정답 - 1을 출력(해당 위치는 2번 세어졌기 때문)
