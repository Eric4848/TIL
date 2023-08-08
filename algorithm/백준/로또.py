from itertools import combinations   # 조합을 사용하기 위해 추가

nums = list(map(int, input().split()))   # 첫째줄을 입력받아
length = nums[0]   # 길이인 첫번째 자리 숫자를 저장하고
nums = nums[1:length+1]   # 첫번째 자리 숫자를 뺀 숫자들만 저장하여
for comb in combinations(nums, 6):   # 6개짜리 조합을 구해서
    print(*comb)   # 출력한다
while True:   # 그 이후로
    nums = list(map(int, input().split()))   # 입력을 받아서
    if len(nums) == 1:   # 길이가 1이면 -> 0 하나만 들어온 경우
        break   # 중단한다
    length = nums[0]   # 아닌경우 마찬가지로 진행한다
    nums = nums[1:length+1]
    print('')   # 문제 조건에 의해 공백 한 줄을 출력한다
    for comb in combinations(nums, 6):
        print(*comb)
