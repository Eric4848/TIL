N = int(input())
nums = [1] * 1100001   # 소수를 판별할 리스트(정답이 입력보다 클 수도 있으므로)
nums[1] = 0   # 1은 소수가 아니다


# 펠린드롬을 확인하는 함수
def chk(n):
    tmp = str(n)   # 입력된 숫자를 문자로 바꾸어
    for i in range(len(tmp) // 2):   # 길이의 반만큼(홀수인 경우 가운데는 안해도 된다)
        if tmp[i] != tmp[-1-i]:   # 양끝부터 하나씩 비교하며 다른경우
            return False   # 아니다를 반환
    return True   # 다 같은 경우 맞다를 반환


# 소수 판별
for i in range(2, int(1100001 ** 0.5)):   # 소수의 루트만큼
    if nums[i]:   # 소수이면
        for j in range(i * i, 1100001, i):   # 그 수의 제곱부터(이전은 앞에서 계산했으므로) 자기 자신만큼 간격으로
            nums[j] = 0   # 소수가 아님 처리

# 펠린드롬 확인
for i in range(N, 1100001):
    if nums[i]:   # 소수라면
        if chk(i):   # 판별하여 맞는경우
            print(i)   # 정답 출력
            break
