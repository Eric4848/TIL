import sys

sys.setrecursionlimit(10 ** 9)
nums = []   # 출력된 숫자를 저장할 리스트
while True:
    try:
        num = int(input())   # 숫자를 입력받아
        nums.append(num)   # 출력된 숫자 리스트에 저장
    except:   # 숫자가 입력되지 않는다면
        break   # 중단


def check(arr):   # 트리를 확인할 함수
    if len(arr) == 0:   # 입력된 리스트가 비어있다면
        return   # 중단

    mid = arr[0]   # 두 수의 중간이 되는 상위 노드숫자
    arrL, arrR = arr[1:], []   # 하위의 좌, 우 숫자들의 리스트 / 중간보다 큰 것을 확인하므로 일단 모두 작다고 가정
    for i in range(1, len(arr)):    # 하위 숫자들 중
        if mid < arr[i]:   # 중간값보다 큰 값이 있다면
            arrL = arr[1:i]   # 그 값 전까지 작은 하위노드
            arrR = arr[i:]   # 그 값부터 큰 하위노드로 설정 후
            break   # 노드확인 중단

    check(arrL)   # 작은 하위노드 확인
    check(arrR)   # 큰 하위노드 확인
    print(mid)   # 중간 값 출력


check(nums)
