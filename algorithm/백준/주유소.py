N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
minimum = float('inf')   # 기름 가격의 최소치를 초기화
answer = 0   # 총 주유금액을 초기화

for i in range(N-1):
    if prices[i] < minimum:   # 현 주유소 가격이 최저가보다 싸면
        minimum = prices[i]   # 기름 가격을 갱신해준다
    answer += minimum * distances[i]   # 총 주유금액에 기름 가격과 거리의 곱을 더해준다

print(answer)
