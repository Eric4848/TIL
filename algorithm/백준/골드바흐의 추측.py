sosu = [1] * 10001   # 10000보다 작거나 같은 수를 계산하기때문에 10001개의 리스트 생성
sosu[0], sosu[1] = 0, 0   # 0, 1은 소수가 아니므로 0으로 초기화
for i in range(2, 101):   # 2부터 10000의 루트값인 100까지
    if sosu[i] == 1:   # 소수이면
        for j in range(i * 2, 10001, i):   # 소수의 n배한 수를
            sosu[j] = 0   # 0으로 초기화
N = int(input())
for _ in range(N):
    num = int(input())
    a = num // 2   # 짝수로 주어지기때문에 몫이 항상 정수이다
    b = num // 2
    for _ in range(5000):   # 10000의 반인 5000만큼
        if sosu[a] == 1 and sosu[b] == 1:   # 둘 다 소수이면
            print(a, b)   # 출력
            break
        a -= 1   # 아닌경우 1씩 증감 해준다
        b += 1
